$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Modes = @("direct12","prefix19","nielsen12")

function Parse-Mode([string]$Mode) {
  $Work = Join-Path $Lab ("gowin_1_9_9b4\" + $Mode)
  if (!(Test-Path $Work)) {
    throw "Gowin work directory not found: $Work"
  }

  $Rsc = Get-ChildItem -Path (Join-Path $Work "impl\gwsynthesis") -Filter "*_syn_rsc.xml" -File |
    Select-Object -First 1
  $Rpt = Get-ChildItem -Path (Join-Path $Work "impl\gwsynthesis") -Filter "*_syn.rpt.html" -File |
    Select-Object -First 1

  if (!$Rsc) { throw "Gowin synthesis resource XML not found for $Mode" }
  if (!$Rpt) { throw "Gowin synthesis HTML report not found for $Mode" }

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
  $m = [regex]::Match(
    $html,
    '(?<logic>\d+)\s*\(\s*(?<lut>\d+)\s+LUT\s*,\s*(?<alu>\d+)\s+ALU\s*\)\s*/\s*(?<cap>\d+)',
    'IgnoreCase'
  )
  if (!$m.Success) {
    throw "Could not parse logic/LUT/ALU/capacity for $Mode"
  }

  $Logic = [int]$m.Groups["logic"].Value
  $Capacity = [int]$m.Groups["cap"].Value
  $RptLut = [int]$m.Groups["lut"].Value
  $RptAlu = [int]$m.Groups["alu"].Value

  if ($RptLut -ne $Lut -or $RptAlu -ne $Alu) {
    throw ("Resource parser disagreement for {0}: XML LUT/ALU={1}/{2}, report={3}/{4}" -f $Mode,$Lut,$Alu,$RptLut,$RptAlu)
  }

  $Project = "h19_" + $Mode + "_gw5a25_syn"
  $PrimaryLog = Join-Path $Work ($Project + ".log")
  if (!(Test-Path $PrimaryLog)) {
    throw "Primary Gowin transcript not found for $Mode"
  }

  $finish = @(Select-String -Path $PrimaryLog -SimpleMatch "GowinSynthesis finish").Count
  $ex3791 = @(Select-String -Path $PrimaryLog -SimpleMatch "EX3791").Count

  [pscustomobject]@{
    Mode = $Mode
    Synthesis = if ($finish -gt 0) { "PASS" } else { "UNKNOWN" }
    Logic = $Logic
    LogicCapacity = $Capacity
    LogicPct = [math]::Round(100.0 * $Logic / $Capacity, 2)
    LUT = $Lut
    ALU = $Alu
    Registers = $Registers
    DSP = $Dsp
    EX3791 = $ex3791
  }
}

$Rows = foreach ($Mode in $Modes) { Parse-Mode $Mode }

$D = $Rows | Where-Object Mode -eq "direct12"
$P = $Rows | Where-Object Mode -eq "prefix19"
$N = $Rows | Where-Object Mode -eq "nielsen12"

$resourceFields = @("Logic","LUT","ALU","Registers","DSP")
$dpEqual = $true
foreach ($f in $resourceFields) {
  if ($D.$f -ne $P.$f) { $dpEqual = $false }
}

$quotient = if ($dpEqual -and (
    $N.Logic -ne $D.Logic -or
    $N.LUT -ne $D.LUT -or
    $N.ALU -ne $D.ALU -or
    $N.Registers -ne $D.Registers -or
    $N.DSP -ne $D.DSP
  )) {
  "{{D,P},{N}}"
} elseif (
  $D.Logic -eq $P.Logic -and $D.Logic -eq $N.Logic -and
  $D.LUT -eq $P.LUT -and $D.LUT -eq $N.LUT -and
  $D.ALU -eq $P.ALU -and $D.ALU -eq $N.ALU -and
  $D.Registers -eq $P.Registers -and $D.Registers -eq $N.Registers -and
  $D.DSP -eq $P.DSP -and $D.DSP -eq $N.DSP
) {
  "{{D,P,N}}"
} else {
  "{{D},{P},{N}} or mixed observer partition"
}

$DeltaLogic = $N.Logic - $D.Logic
$DeltaLogicPct = [math]::Round(100.0 * $DeltaLogic / $D.Logic, 2)
$DeltaLut = $N.LUT - $D.LUT
$DeltaLutPct = [math]::Round(100.0 * $DeltaLut / $D.LUT, 2)
$DeltaAlu = $N.ALU - $D.ALU
$DeltaAluPct = [math]::Round(100.0 * $DeltaAlu / $D.ALU, 2)

$Csv = Join-Path $Lab "H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.csv"
$Md = Join-Path $Lab "H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.md"

$Rows | Export-Csv -NoTypeInformation -Encoding UTF8 $Csv

$mdLines = @()
$mdLines += "# H19-LAB-02 Gowin synthesis summary"
$mdLines += ""
$mdLines += 'Target: `GW5A-25A / GW5A-LV25MG121NC1/I0`'
$mdLines += ""
$mdLines += "| Mode | Synthesis | Logic | Capacity | Logic % | LUT | ALU | Registers | DSP | EX3791 |"
$mdLines += "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
foreach ($r in $Rows) {
  $mdLines += ("| {0} | {1} | {2} | {3} | {4:N2} | {5} | {6} | {7} | {8} | {9} |" -f
    $r.Mode,$r.Synthesis,$r.Logic,$r.LogicCapacity,$r.LogicPct,$r.LUT,$r.ALU,$r.Registers,$r.DSP,$r.EX3791)
}
$mdLines += ""
$mdLines += ('Measured synthesis-resource quotient: `{0}`' -f $quotient)
$mdLines += ""
$mdLines += ("NIELSEN12 vs DIRECT12/PREFIX19: Logic {0:+#;-#;0} ({1:+0.00;-0.00;0.00}%), LUT {2:+#;-#;0} ({3:+0.00;-0.00;0.00}%), ALU {4:+#;-#;0} ({5:+0.00;-0.00;0.00}%)." -f
  $DeltaLogic,$DeltaLogicPct,$DeltaLut,$DeltaLutPct,$DeltaAlu,$DeltaAluPct)
$mdLines += ""
$mdLines += "Claim boundary: this quotient is for the declared Gowin synthesis resource observer only. It is not a netlist-identity claim and not yet a post-P&R physical quotient."
$mdLines += ""
$mdLines += "The four EX3791 warnings per mode arise from the frozen H17-08 helper RTL narrowing reduced integer values into 3-bit mod-7 results; the RTL is intentionally unchanged from the cross-tool experiment."

Set-Content -Path $Md -Value $mdLines -Encoding UTF8

Write-Host ""
Write-Host "== H19-LAB-02 GOWIN SYNTHESIS FAMILY =="
$Rows | Format-Table -AutoSize
Write-Host ""
Write-Host ("Resource quotient: {0}" -f $quotient)
Write-Host ("N vs D/P Logic: {0:+#;-#;0} ({1:+0.00;-0.00;0.00}%)" -f $DeltaLogic,$DeltaLogicPct)
Write-Host ("N vs D/P LUT:   {0:+#;-#;0} ({1:+0.00;-0.00;0.00}%)" -f $DeltaLut,$DeltaLutPct)
Write-Host ("N vs D/P ALU:   {0:+#;-#;0} ({1:+0.00;-0.00;0.00}%)" -f $DeltaAlu,$DeltaAluPct)
Write-Host ("CSV: {0}" -f $Csv)
Write-Host ("MD:  {0}" -f $Md)

if ($quotient -ne "{{D,P},{N}}") {
  throw "Unexpected Gowin synthesis-resource quotient: $quotient"
}

Write-Host "PASS: H19-LAB-02 Gowin synthesis family closed as {{D,P},{N}}"
