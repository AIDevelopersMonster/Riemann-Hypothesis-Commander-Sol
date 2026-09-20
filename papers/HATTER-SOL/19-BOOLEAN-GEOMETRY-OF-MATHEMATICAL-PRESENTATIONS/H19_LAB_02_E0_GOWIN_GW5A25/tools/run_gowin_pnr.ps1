param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("direct12","prefix19","nielsen12")]
  [string]$Mode
)

$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$H19 = (Resolve-Path (Join-Path $Lab "..")).Path
$Hatter = (Resolve-Path (Join-Path $H19 "..")).Path
$H17 = Join-Path $Hatter "17-NONABELIAN-TOMOGRAPHY-HARDWARE"

$GwSh = "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe"
if (!(Test-Path $GwSh)) { throw "Gowin gw_sh.exe not found at $GwSh" }

$Gen = Join-Path $Lab ("generated\" + $Mode)
$Work = Join-Path $Lab ("gowin_1_9_9b4_pnr\" + $Mode)
$Project = "h19_" + $Mode + "_gw5a25_pnr"

New-Item -ItemType Directory -Force $Gen | Out-Null
New-Item -ItemType Directory -Force $Work | Out-Null

Write-Host "== H19-LAB-02 GOWIN P&R CALIBRATION =="
Write-Host ("Mode: {0}" -f $Mode)
Write-Host "Target: GW5A-25A / GW5A-LV25MG121NC1/I0"
Write-Host "Tool: Gowin Education 1.9.9Beta-4"
Write-Host "Clock contract: clk = 100 MHz (SDC period 10.000 ns)"

py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "closure classifier generation failed" }

py -3 (Join-Path $H19 "tools\generate_h19_r12_variants.py") --mode $Mode --out-dir $Gen
if ($LASTEXITCODE -ne 0) { throw "H19 variant generation failed" }

function TclPath([string]$p) {
  return ([System.IO.Path]::GetFullPath($p) -replace '\\','/')
}

$Membership = TclPath (Join-Path $Gen "psl27_membership_only.sv")
$ClassOnly = TclPath (Join-Path $Gen "psl27_member_class_only.sv")
$Core = TclPath (Join-Path $Gen "h18_r12_comb_core.sv")
$Controller = TclPath (Join-Path $Gen "h18_r12_comb_controller.sv")

$SdcFile = Join-Path $Work ($Project + ".sdc")
Set-Content -Path $SdcFile -Value 'create_clock -name clk -period 10.000 [get_ports {clk}]' -Encoding ascii
$Sdc = TclPath $SdcFile

$Snapshot = TclPath (Join-Path $Work ($Project + "_snapshot.tcl"))

$Tcl = @"
set_device GW5A-LV25MG121NC1/I0
add_file {$Membership}
add_file {$ClassOnly}
add_file {$Core}
add_file {$Controller}
add_file {$Sdc}
set_option -top_module h18_r12_comb_controller
set_option -verilog_std sysv2017
set_option -output_base_name $Project
set_option -gen_text_timing_rpt 1
set_option -timing_driven 1
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

  Get-Content $Log
  Write-Host ("H19 {0} GOWIN P&R ELAPSED: {1:N3} seconds" -f $Mode,$sw.Elapsed.TotalSeconds)
  Write-Host ("gw_sh exit code: {0}" -f $rc)

  Write-Host "== GENERATED FILES =="
  Get-ChildItem -Recurse -File |
    Sort-Object FullName |
    Select-Object FullName,Length |
    Format-Table -AutoSize

  Write-Host "== P&R / TIMING / RESOURCE HINTS =="
  Get-ChildItem -Recurse -File |
    Where-Object { $_.Length -lt 20MB } |
    Select-String -Pattern "ERROR","Error","WARNING","Warning","Place","Route","Timing","Fmax","MHz","Slack","Resource","LUT","Register","DSP","ALU" -ErrorAction SilentlyContinue |
    Select-Object -First 300

  if ($rc -ne 0) {
    throw ("Gowin full flow returned exit code {0}" -f $rc)
  }

  Write-Host ("DONE H19-LAB-02 {0}: inspect P&R/timing reports before declaring physical PASS" -f $Mode)
}
finally {
  Pop-Location
}
