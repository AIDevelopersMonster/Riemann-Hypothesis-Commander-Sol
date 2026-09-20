$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Modes = @("direct12","prefix19","nielsen12")

function Parse-Mode([string]$Mode) {
  $Work = Join-Path $Lab ("gowin_1_9_9b4_pnr\" + $Mode)
  $Pnr = Join-Path $Work "impl\pnr"

  if (!(Test-Path $Pnr)) {
    throw "Gowin P&R directory not found: $Pnr"
  }

  $Rpt = Get-ChildItem -Path $Pnr -Filter "*_pnr.rpt.txt" -File | Select-Object -First 1
  $Tr  = Get-ChildItem -Path $Pnr -Filter "*_pnr.tr" -File | Select-Object -First 1
  if (!$Rpt) { throw "P&R resource report not found for $Mode" }
  if (!$Tr)  { throw "P&R timing report not found for $Mode" }

  $rptText = Get-Content -Raw $Rpt.FullName
  $trText  = Get-Content -Raw $Tr.FullName

  function NeedMatch([string]$Text,[string]$Pattern,[string]$Label) {
    $m = [regex]::Match($Text,$Pattern,[System.Text.RegularExpressions.RegexOptions]::Multiline)
    if (!$m.Success) { throw "Could not parse $Label for $Mode" }
    return $m
  }

  $mLogic = NeedMatch $rptText '^\s*Logic\s*\|\s*(\d+)\s*/\s*(\d+)' "Logic"
  $mLutAlu = NeedMatch $rptText 'LUT,ALU,ROM16\s*\|\s*\d+\s*\(\s*(\d+)\s+LUT,\s*(\d+)\s+ALU' "LUT/ALU"
  $mReg = NeedMatch $rptText '^\s*Register\s*\|\s*(\d+)\s*/\s*(\d+)' "Register"
  $mCls = NeedMatch $rptText '^\s*CLS\s*\|\s*(\d+)\s*/\s*(\d+)' "CLS"
  $mIo = NeedMatch $rptText '^\s*I/O Port\s*\|\s*(\d+)' "I/O Port"
  $mDsp = NeedMatch $rptText '^\s*--MULT12X12\s*\|\s*(\d+)' "MULT12X12"

  $mFmax = NeedMatch $trText '^\s*1\s+clk\s+[0-9.]+\(MHz\)\s+([0-9.]+)\(MHz\)\s+(\d+)\s+TOP' "Actual Fmax"
  $mSetupTns = NeedMatch $trText '^\s*clk\s+setup\s+(-?[0-9.]+)\s+(\d+)\s*$' "setup TNS"
  $mHoldTns = NeedMatch $trText '^\s*clk\s+hold\s+(-?[0-9.]+)\s+(\d+)\s*$' "hold TNS"
  $mWns = NeedMatch $trText '^Slack\s*:\s*(-?[0-9.]+)\s*$' "worst setup slack"

  $Project = "h19_" + $Mode + "_gw5a25_pnr"
  $Log = Join-Path $Work ($Project + ".log")
  if (!(Test-Path $Log)) { throw "Primary P&R transcript not found for $Mode" }

  $logText = Get-Content -Raw $Log
  $pnrPass = ($logText -match 'Placement and routing completed') -and ($logText -match 'Bitstream generation completed')

  $logic = [int]$mLogic.Groups[1].Value
  $logicCapacity = [int]$mLogic.Groups[2].Value

  [pscustomobject]@{
    Mode = $Mode
    PnR = if ($pnrPass) { "PASS" } else { "UNKNOWN" }
    Timing100MHz = if ([double]$mWns.Groups[1].Value -ge 0.0) { "PASS" } else { "FAIL" }
    Logic = $logic
    LogicCapacity = $logicCapacity
    LogicPct = [math]::Round(100.0 * $logic / $logicCapacity, 2)
    LUT = [int]$mLutAlu.Groups[1].Value
    ALU = [int]$mLutAlu.Groups[2].Value
    Registers = [int]$mReg.Groups[1].Value
    CLS = [int]$mCls.Groups[1].Value
    IO = [int]$mIo.Groups[1].Value
    DSP = [int]$mDsp.Groups[1].Value
    ActualFmaxMHz = [double]$mFmax.Groups[1].Value
    CriticalLevels = [int]$mFmax.Groups[2].Value
    WNSns = [double]$mWns.Groups[1].Value
    SetupTNSns = [double]$mSetupTns.Groups[1].Value
    SetupEndpoints = [int]$mSetupTns.Groups[2].Value
    HoldTNSns = [double]$mHoldTns.Groups[1].Value
    HoldEndpoints = [int]$mHoldTns.Groups[2].Value
  }
}

$Rows = foreach ($Mode in $Modes) { Parse-Mode $Mode }

$D = $Rows | Where-Object Mode -eq "direct12"
$P = $Rows | Where-Object Mode -eq "prefix19"
$N = $Rows | Where-Object Mode -eq "nielsen12"

$observerFields = @(
  "Logic","LUT","ALU","Registers","CLS","IO","DSP",
  "ActualFmaxMHz","CriticalLevels","WNSns","SetupTNSns",
  "SetupEndpoints","HoldTNSns","HoldEndpoints"
)

$dpEqual = $true
foreach ($f in $observerFields) {
  if ($D.$f -ne $P.$f) { $dpEqual = $false }
}

$nDifferent = $false
foreach ($f in $observerFields) {
  if ($N.$f -ne $D.$f) { $nDifferent = $true }
}

$quotient = if ($dpEqual -and $nDifferent) {
  "{{D,P},{N}}"
} elseif (!$dpEqual -and $nDifferent) {
  "{{D},{P},{N}} or mixed physical partition"
} elseif ($dpEqual -and !$nDifferent) {
  "{{D,P,N}}"
} else {
  "mixed physical partition"
}

$Csv = Join-Path $Lab "H19_LAB02_GOWIN_PNR_SUMMARY.csv"
$Md = Join-Path $Lab "H19_LAB02_GOWIN_PNR_SUMMARY.md"

$Rows | Export-Csv -NoTypeInformation -Encoding UTF8 $Csv

$mdLines = @()
$mdLines += "# H19-LAB-02 Gowin post-P&R physical summary"
$mdLines += ""
$mdLines += 'Target: `GW5A-25A / GW5A-LV25MG121NC1/I0`'
$mdLines += ""
$mdLines += 'Clock contract: `clk = 100 MHz` via `create_clock -period 10.000`.'
$mdLines += ""
$mdLines += "| Mode | P&R | 100 MHz | Logic | Logic % | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | setup TNS ns | setup EP | hold TNS ns |"
$mdLines += "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
foreach ($r in $Rows) {
  $mdLines += ("| {0} | {1} | {2} | {3} | {4:N2} | {5} | {6} | {7} | {8} | {9} | {10:N3} | {11} | {12:N3} | {13:N3} | {14} | {15:N3} |" -f
    $r.Mode,$r.PnR,$r.Timing100MHz,$r.Logic,$r.LogicPct,$r.LUT,$r.ALU,$r.Registers,$r.CLS,$r.DSP,$r.ActualFmaxMHz,$r.CriticalLevels,$r.WNSns,$r.SetupTNSns,$r.SetupEndpoints,$r.HoldTNSns)
}
$mdLines += ""
$mdLines += ('Measured post-P&R physical quotient: `{0}`' -f $quotient)
$mdLines += ""
$mdLines += "Claim boundary: equality means equality of the declared measured physical-profile vector, not identity of routed netlists, placements, bitstreams, or all physical state."
$mdLines += ""
$mdLines += "All three variants completed placement, routing, timing analysis, and bitstream generation. A P&R PASS does not imply the 100 MHz constraint is met; timing status is reported separately."

Set-Content -Path $Md -Value $mdLines -Encoding UTF8

Write-Host ""
Write-Host "== H19-LAB-02 GOWIN POST-P&R FAMILY =="
$Rows | Format-Table -AutoSize
Write-Host ""
Write-Host ("Physical quotient: {0}" -f $quotient)
Write-Host ("CSV: {0}" -f $Csv)
Write-Host ("MD:  {0}" -f $Md)

if ($quotient -ne "{{D,P},{N}}") {
  throw "Unexpected Gowin post-P&R physical quotient: $quotient"
}

Write-Host "PASS: H19-LAB-02 Gowin post-P&R family closed as {{D,P},{N}}"
