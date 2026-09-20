param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("direct12","prefix19","nielsen12")]
  [string]$Mode
)

$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Work = Join-Path $Lab ("gowin_1_9_9b4\" + $Mode)

if (!(Test-Path $Work)) {
  throw "Gowin work directory not found: $Work"
}

$Rsc = Get-ChildItem -Path (Join-Path $Work "impl\gwsynthesis") -Filter "*_syn_rsc.xml" -File |
  Select-Object -First 1
$Rpt = Get-ChildItem -Path (Join-Path $Work "impl\gwsynthesis") -Filter "*_syn.rpt.html" -File |
  Select-Object -First 1

if (!$Rsc) { throw "Gowin synthesis resource XML not found under $Work" }
if (!$Rpt) { throw "Gowin synthesis HTML report not found under $Work" }

[xml]$xml = Get-Content -Raw $Rsc.FullName
$nodes = $xml.SelectNodes('//*[@Register or @Lut or @Alu or @Dsp]')

function AttrInt($node, [string]$name) {
  $v = $node.GetAttribute($name)
  if ([string]::IsNullOrWhiteSpace($v)) { return 0 }
  return [int]$v
}

$Registers = 0
$Lut = 0
$Alu = 0
$Dsp = 0
foreach ($n in $nodes) {
  $Registers += AttrInt $n "Register"
  $Lut += AttrInt $n "Lut"
  $Alu += AttrInt $n "Alu"
  $Dsp += AttrInt $n "Dsp"
}

$html = Get-Content -Raw $Rpt.FullName
$logicUsed = $null
$logicCapacity = $null
$logicPct = $null

$m = [regex]::Match($html, '(?<logic>\d+)\s*\(\s*(?<lut>\d+)\s+LUT\s*,\s*(?<alu>\d+)\s+ALU\s*\)\s*/\s*(?<cap>\d+)', 'IgnoreCase')
if ($m.Success) {
  $logicUsed = [int]$m.Groups["logic"].Value
  $logicCapacity = [int]$m.Groups["cap"].Value
  if ($logicCapacity -gt 0) {
    $logicPct = [math]::Round(100.0 * $logicUsed / $logicCapacity, 2)
  }

  # Cross-check XML aggregation against the synthesis report.
  $rptLut = [int]$m.Groups["lut"].Value
  $rptAlu = [int]$m.Groups["alu"].Value
  if ($rptLut -ne $Lut -or $rptAlu -ne $Alu) {
    throw ("Resource parser disagreement: XML LUT/ALU={0}/{1}, report LUT/ALU={2}/{3}" -f $Lut,$Alu,$rptLut,$rptAlu)
  }
}

$Project = "h19_" + $Mode + "_gw5a25_syn"
$PrimaryLog = Join-Path $Work ($Project + ".log")
if (!(Test-Path $PrimaryLog)) {
  throw "Primary Gowin transcript not found: $PrimaryLog"
}

$finishCount = @(Select-String -Path $PrimaryLog -SimpleMatch "GowinSynthesis finish" -ErrorAction SilentlyContinue).Count
$warn3791 = @(Select-String -Path $PrimaryLog -SimpleMatch "EX3791" -ErrorAction SilentlyContinue).Count

$status = if ($finishCount -gt 0) { "PASS" } else { "UNKNOWN" }

$row = [pscustomobject]@{
  Mode = $Mode
  Synthesis = $status
  Logic = $logicUsed
  LogicCapacity = $logicCapacity
  LogicPct = $logicPct
  LUT = $Lut
  ALU = $Alu
  Registers = $Registers
  DSP = $Dsp
  EX3791 = $warn3791
}

Write-Host ""
Write-Host "== H19-LAB-02 GOWIN SYNTHESIS SUMMARY =="
$row | Format-Table -AutoSize
Write-Host ("Resource XML: {0}" -f $Rsc.FullName)
Write-Host ("HTML report:  {0}" -f $Rpt.FullName)

if ($status -ne "PASS") {
  throw "Could not confirm GowinSynthesis finish in the local logs"
}

Write-Host ("PASS: parsed H19-LAB-02 {0} synthesis resources" -f $Mode)
