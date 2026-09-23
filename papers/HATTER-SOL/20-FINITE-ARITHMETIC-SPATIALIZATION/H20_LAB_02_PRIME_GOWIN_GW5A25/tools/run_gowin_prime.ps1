param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("direct","balanced","linear")]
  [string]$Mode,

  [Parameter(Mandatory=$true)]
  [ValidateSet(8,9,10)]
  [int]$Width
)

$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$H20 = (Resolve-Path (Join-Path $Lab "..")).Path

$GwSh = "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe"
if (!(Test-Path $GwSh)) { throw "Gowin gw_sh.exe not found at $GwSh" }

$GenRoot = Join-Path $Lab "generated"
$WDir = Join-Path $GenRoot ("w{0}" -f $Width)
$Work = Join-Path $Lab ("gowin_1_9_9b4_pnr\w{0}_{1}" -f $Width,$Mode)
$Project = "h20_w{0}_{1}_gw5a25_pnr" -f $Width,$Mode

New-Item -ItemType Directory -Force $GenRoot | Out-Null
New-Item -ItemType Directory -Force $Work | Out-Null

Write-Host "== H20-LAB-02 PRIME GOWIN P&R =="
Write-Host ("Width: W={0}" -f $Width)
Write-Host ("Mode: {0}" -f $Mode)
Write-Host "Target: GW5A-25A / GW5A-LV25MG121NC1/I0"
Write-Host "Tool: Gowin Education 1.9.9Beta-4"
Write-Host "Clock contract: clk = 100 MHz (SDC period 10.000 ns)"

py -3 (Join-Path $H20 "tools\generate_prime_spatial_lab.py") --out-dir $GenRoot --widths $Width
if ($LASTEXITCODE -ne 0) { throw "prime RTL generation failed" }

$Source = Join-Path $WDir ("nextprime_{0}.sv" -f $Mode)
if (!(Test-Path $Source)) { throw "generated source missing: $Source" }

$Wrapper = Join-Path $Work "nextprime_registered_top.sv"
$OW = $Width + 1
$WrapperText = @"
module nextprime_registered_top(
  input  logic clk,
  input  logic [$($Width-1):0] x,
  output logic [$($OW-1):0] p
);
  logic [$($Width-1):0] x_q;
  logic [$($OW-1):0] p_comb;

  always_ff @(posedge clk) begin
    x_q <= x;
    p   <= p_comb;
  end

  nextprime_top u_core(
    .x(x_q),
    .p(p_comb)
  );
endmodule
"@
Set-Content -Path $Wrapper -Value $WrapperText -Encoding ascii

function TclPath([string]$p) {
  return ([System.IO.Path]::GetFullPath($p) -replace '\\','/')
}

$SdcFile = Join-Path $Work ($Project + ".sdc")
Set-Content -Path $SdcFile -Value 'create_clock -name clk -period 10.000 [get_ports {clk}]' -Encoding ascii

$SourceT = TclPath $Source
$WrapperT = TclPath $Wrapper
$SdcT = TclPath $SdcFile
$Snapshot = TclPath (Join-Path $Work ($Project + "_snapshot.tcl"))

$Tcl = @"
set_device GW5A-LV25MG121NC1/I0
add_file {$SourceT}
add_file {$WrapperT}
add_file {$SdcT}
set_option -top_module nextprime_registered_top
set_option -verilog_std sysv2017
set_option -output_base_name $Project
set_option -gen_text_timing_rpt 1
set_option -timing_driven 1
set_option -use_mspi_as_gpio 1
set_option -use_ready_as_gpio 1
saveto -all_options {$Snapshot}
run all
"@

$Flow = Join-Path $Work ($Project + ".tcl")
$Log = Join-Path $Work ($Project + ".log")
Set-Content -Path $Flow -Value $Tcl -Encoding ascii

Push-Location $Work
try {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $GwSh $Flow *> $Log
  $rc = $LASTEXITCODE
  $sw.Stop()

  Write-Host ("H20 W={0} {1} GOWIN P&R ELAPSED: {2:N3} seconds" -f $Width,$Mode,$sw.Elapsed.TotalSeconds)
  Write-Host ("gw_sh exit code: {0}" -f $rc)

  if ($rc -ne 0) {
    Get-Content $Log
    throw ("Gowin full flow returned exit code {0}" -f $rc)
  }

  $Pnr = Join-Path $Work "impl\pnr"
  $Rpt = Get-ChildItem -Path $Pnr -Filter "*_pnr.rpt.txt" -File | Select-Object -First 1
  $Tr  = Get-ChildItem -Path $Pnr -Filter "*_pnr.tr" -File | Select-Object -First 1

  if (!$Rpt) { throw "P&R resource report not found" }
  if (!$Tr)  { throw "P&R timing report not found" }

  $rptText = Get-Content -Raw $Rpt.FullName
  $trText  = Get-Content -Raw $Tr.FullName
  $logText = Get-Content -Raw $Log

  function TryMatch([string]$Text,[string]$Pattern) {
    return [regex]::Match($Text,$Pattern,[System.Text.RegularExpressions.RegexOptions]::Multiline)
  }

  $mLogic = TryMatch $rptText '^\s*Logic\s*\|\s*(\d+)\s*/\s*(\d+)'
  $mLutAlu = TryMatch $rptText 'LUT,ALU,ROM16\s*\|\s*\d+\s*\(\s*(\d+)\s+LUT,\s*(\d+)\s+ALU(?:,\s*(\d+)\s+ROM16)?'
  $mReg = TryMatch $rptText '^\s*Register\s*\|\s*(\d+)\s*/\s*(\d+)'
  $mCls = TryMatch $rptText '^\s*CLS\s*\|\s*(\d+)\s*/\s*(\d+)'
  $mDsp = TryMatch $rptText '^\s*--MULT12X12\s*\|\s*(\d+)'
  $mBsr = TryMatch $rptText '^\s*(?:BSRAM|Block SRAM|--BSRAM)\s*\|\s*(\d+)'

  $mFmax = TryMatch $trText '^\s*1\s+clk\s+[0-9.]+\(MHz\)\s+([0-9.]+)\(MHz\)\s+(\d+)\s+TOP'
  $mSetupTns = TryMatch $trText '^\s*clk\s+setup\s+(-?[0-9.]+)\s+(\d+)\s*$'
  $mHoldTns = TryMatch $trText '^\s*clk\s+hold\s+(-?[0-9.]+)\s+(\d+)\s*$'
  $mWns = TryMatch $trText '^Slack\s*:\s*(-?[0-9.]+)\s*$'

  $pnrPass = ($logText -match 'Placement and routing completed') -and ($logText -match 'Bitstream generation completed')

  Write-Host ""
  Write-Host "== H20 GOWIN DECLARED PHYSICAL OBSERVER =="
  Write-Host ("P&R pass: {0}" -f $pnrPass)
  if ($mLogic.Success) { Write-Host ("Logic: {0} / {1}" -f $mLogic.Groups[1].Value,$mLogic.Groups[2].Value) }
  if ($mLutAlu.Success) {
    $rom16 = if ($mLutAlu.Groups.Count -gt 3 -and $mLutAlu.Groups[3].Success) { $mLutAlu.Groups[3].Value } else { "0/not reported" }
    Write-Host ("LUT: {0}; ALU: {1}; ROM16: {2}" -f $mLutAlu.Groups[1].Value,$mLutAlu.Groups[2].Value,$rom16)
  }
  if ($mReg.Success) { Write-Host ("Registers: {0}" -f $mReg.Groups[1].Value) }
  if ($mCls.Success) { Write-Host ("CLS: {0}" -f $mCls.Groups[1].Value) }
  if ($mBsr.Success) { Write-Host ("BSRAM: {0}" -f $mBsr.Groups[1].Value) }
  if ($mDsp.Success) { Write-Host ("DSP MULT12X12: {0}" -f $mDsp.Groups[1].Value) }
  if ($mFmax.Success) {
    Write-Host ("Actual Fmax: {0} MHz" -f $mFmax.Groups[1].Value)
    Write-Host ("Critical levels: {0}" -f $mFmax.Groups[2].Value)
  }
  if ($mWns.Success) { Write-Host ("WNS: {0} ns" -f $mWns.Groups[1].Value) }
  if ($mSetupTns.Success) { Write-Host ("Setup TNS: {0} ns; endpoints: {1}" -f $mSetupTns.Groups[1].Value,$mSetupTns.Groups[2].Value) }
  if ($mHoldTns.Success) { Write-Host ("Hold TNS: {0} ns; endpoints: {1}" -f $mHoldTns.Groups[1].Value,$mHoldTns.Groups[2].Value) }

  Write-Host ""
  Write-Host "== RESOURCE LINES =="
  Select-String -Path $Rpt.FullName -Pattern "Logic","LUT,ALU,ROM16","Register","CLS","BSRAM","RAM","MULT12X12" |
    Select-Object -First 80 | ForEach-Object { $_.Line }

  Write-Host ""
  Write-Host "== TIMING SUMMARY =="
  Select-String -Path $Tr.FullName -Pattern "Clock Summary","Max Frequency Summary","Actual Fmax","setup","hold","Slack" -Context 0,8 |
    Select-Object -First 120

  if (!$pnrPass) { throw "Gowin transcript does not confirm placement/routing and bitstream completion" }

  Write-Host ("PASS H20-LAB-02 W={0} {1} on GW5A-LV25MG121NC1/I0" -f $Width,$Mode)
}
finally {
  Pop-Location
}
