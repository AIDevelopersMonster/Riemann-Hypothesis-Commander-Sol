param(
  [string]$CsvPath = "",
  [string]$MarkdownPath = "",
  [string]$PartitionCsvPath = ""
)

$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")

if ([string]::IsNullOrWhiteSpace($CsvPath)) {
  $CsvPath = Join-Path $Lab "H19_LAB01_CYCLONEV_SUMMARY.csv"
}
if ([string]::IsNullOrWhiteSpace($MarkdownPath)) {
  $MarkdownPath = Join-Path $Lab "H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md"
}
if ([string]::IsNullOrWhiteSpace($PartitionCsvPath)) {
  $PartitionCsvPath = Join-Path $Lab "H19_LAB01_PHYSICAL_PARTITIONS.csv"
}

if (!(Test-Path $CsvPath)) { throw "Missing summary CSV: $CsvPath" }

$rows = @(Import-Csv $CsvPath)
$modeOrder = @("direct12","prefix19","nielsen12")
$label = @{ direct12 = "D"; prefix19 = "P"; nielsen12 = "N" }

foreach ($mode in $modeOrder) {
  if (!($rows | Where-Object { $_.Mode -eq $mode })) {
    throw "Summary CSV is missing mode: $mode"
  }
}

$metrics = @(
  "ALM",
  "Registers",
  "DSP",
  "Fmax_MHz",
  "DataDelay_ns",
  "LogicLevels",
  "Cell_ns",
  "Routing_ns"
)

function Normalize-Value([object]$v) {
  if ($null -eq $v) { return "<missing>" }
  $s = ([string]$v).Trim()
  if ([string]::IsNullOrWhiteSpace($s)) { return "<missing>" }
  return $s.Replace(",","")
}

$orderedRows = @()
foreach ($m in $modeOrder) {
  $orderedRows += $rows | Where-Object { $_.Mode -eq $m } | Select-Object -First 1
}

foreach ($r in $orderedRows) {
  if ($r.Fit -ne "FIT") {
    throw ("Physical atlas requires FIT for all modes; {0} has Fit={1}" -f $r.Mode,$r.Fit)
  }
}

function Get-Partition([string]$property) {
  $groups = @()
  $used = @{}
  foreach ($r in $orderedRows) {
    $m = [string]$r.Mode
    if ($used.ContainsKey($m)) { continue }
    $v = Normalize-Value $r.$property
    $members = @()
    foreach ($s in $orderedRows) {
      if ((Normalize-Value $s.$property) -eq $v) {
        $members += [string]$s.Mode
      }
    }
    foreach ($member in $members) { $used[$member] = $true }
    $groups += ,@($members)
  }
  return ,$groups
}

function Get-JointPartition([string[]]$properties) {
  $keys = @{}
  foreach ($r in $orderedRows) {
    $parts = @()
    foreach ($p in $properties) {
      $parts += ("{0}={1}" -f $p,(Normalize-Value $r.$p))
    }
    $keys[[string]$r.Mode] = ($parts -join "|")
  }

  $groups = @()
  $used = @{}
  foreach ($r in $orderedRows) {
    $m = [string]$r.Mode
    if ($used.ContainsKey($m)) { continue }
    $k = $keys[$m]
    $members = @()
    foreach ($s in $orderedRows) {
      $sm = [string]$s.Mode
      if ($keys[$sm] -eq $k) { $members += $sm }
    }
    foreach ($member in $members) { $used[$member] = $true }
    $groups += ,@($members)
  }
  return ,$groups
}

function Partition-ToText($partition) {
  $blocks = @()
  foreach ($g in $partition) {
    $names = @()
    foreach ($m in $g) { $names += $label[$m] }
    $blocks += ("{" + ($names -join ",") + "}")
  }
  return "{" + ($blocks -join ",") + "}"
}

function Pair-Count($partition) {
  $q = 0
  foreach ($g in $partition) {
    $n = @($g).Count
    $q += [int](($n * ($n - 1)) / 2)
  }
  return $q
}

$availableMetrics = @()
foreach ($metric in $metrics) {
  $ok = $true
  foreach ($r in $orderedRows) {
    if ((Normalize-Value $r.$metric) -eq "<missing>") { $ok = $false }
  }
  if ($ok) { $availableMetrics += $metric }
}

if ($availableMetrics.Count -eq 0) {
  throw "No complete physical metric is available across all three modes"
}

$jointPartition = Get-JointPartition $availableMetrics
$jointPairCount = Pair-Count $jointPartition
$jointText = Partition-ToText $jointPartition

$partitionRows = @()
$visibilityBits = @()

foreach ($metric in $availableMetrics) {
  $part = Get-Partition $metric
  $q = Pair-Count $part
  $gap = $q - $jointPairCount

  $d = $orderedRows | Where-Object { $_.Mode -eq "direct12" } | Select-Object -First 1
  $p = $orderedRows | Where-Object { $_.Mode -eq "prefix19" } | Select-Object -First 1
  $visibleDP = if ((Normalize-Value $d.$metric) -ne (Normalize-Value $p.$metric)) { 1 } else { 0 }
  $visibilityBits += $visibleDP

  $partitionRows += [pscustomobject]@{
    Observer = $metric
    Partition = Partition-ToText $part
    ClassCount = @($part).Count
    IndistinguishablePairs = $q
    JointProfilePairCount = $jointPairCount
    ProfileRelativeLatentGap = $gap
    DirectPrefixVisible = $visibleDP
  }
}

$partitionRows | Export-Csv -NoTypeInformation -Encoding UTF8 $PartitionCsvPath

function Esc([object]$v) {
  if ($null -eq $v) { return "" }
  return ([string]$v).Replace("|","\|")
}

$md = New-Object System.Collections.Generic.List[string]
$md.Add("# H19-LAB-01 · Physical Visibility Atlas")
$md.Add("")
$md.Add("Status: AUTO-GENERATED FROM MATCHED CYCLONE-V REPORTS")
$md.Add("")
$md.Add("Target: 5CEFA7F23C6")
$md.Add("Tool: Quartus II 13.1")
$md.Add("Reference constraint: 100 MHz")
$md.Add("Timing protocol: Slow 1100 mV / 85 C")
$md.Add("")
$md.Add("Presentations: D = DIRECT12; P = PREFIX19; N = NIELSEN12.")
$md.Add("")
$md.Add("All equality and partition statements below are at the finite precision printed by the frozen Quartus reporting flow.")
$md.Add("")
$md.Add("## 1. Matched physical profile")
$md.Add("")
$md.Add("| mode | ALM | registers | DSP | Fmax MHz | data delay ns | logic levels | cell ns | routing ns |")
$md.Add("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
foreach ($r in $orderedRows) {
  $md.Add(("| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |" -f
    $label[$r.Mode],(Esc $r.ALM),(Esc $r.Registers),(Esc $r.DSP),(Esc $r.Fmax_MHz),
    (Esc $r.DataDelay_ns),(Esc $r.LogicLevels),(Esc $r.Cell_ns),(Esc $r.Routing_ns)))
}
$md.Add("")
$md.Add("## 2. Physical observer partitions")
$md.Add("")
$md.Add("| observer | partition | classes | indistinguishable pairs | profile-relative latent gap | D/P visible |")
$md.Add("| --- | --- | ---: | ---: | ---: | ---: |")
foreach ($pr in $partitionRows) {
  $md.Add(("| {0} | {1} | {2} | {3} | {4} | {5} |" -f
    $pr.Observer,$pr.Partition,$pr.ClassCount,$pr.IndistinguishablePairs,
    $pr.ProfileRelativeLatentGap,$pr.DirectPrefixVisible))
}
$md.Add("")
$md.Add("## 3. Finest measured joint physical profile")
$md.Add("")
$md.Add(("Available coordinates: {0}." -f ($availableMetrics -join ", ")))
$md.Add("")
$md.Add(("Joint-profile partition: {0}." -f $jointText))
$md.Add("")
$md.Add(("Joint-profile indistinguishable-pair count: {0}." -f $jointPairCount))
$md.Add("")
$md.Add("This joint profile is the finest measured observer in this laboratory. It is not identified with the complete routed FPGA implementation state.")
$md.Add("")
$md.Add("ProfileRelativeLatentGap means Q(single-coordinate partition) minus Q(joint measured-profile partition), not a claim about hidden distinctions in the full Quartus database.")
$md.Add("")
$md.Add("## 4. DIRECT12 / PREFIX19 physical visibility vector")
$md.Add("")
$md.Add(("Coordinate order: {0}." -f ($availableMetrics -join ", ")))
$md.Add("")
$md.Add(("Visibility vector: ({0})." -f ($visibilityBits -join ",")))
$md.Add("")
$md.Add("A 1 means the printed Quartus values differ; a 0 means they coincide at the frozen report precision.")
$md.Add("")
$md.Add("## 5. Interpretation rule")
$md.Add("")
$md.Add("Do not collapse this atlas to one scalar winner. ALM, DSP, register count, Fmax, logic depth, cell delay and routing delay are different physical observers and may induce different presentation partitions.")
$md.Add("")
$md.Add("The scientifically relevant object is the family O_phys -> P_phys(O_phys), together with the joint measured-profile partition.")
$md.Add("")
$md.Add("## 6. Publication boundary")
$md.Add("")
$md.Add("This report is a technology/tool/constraint-relative realization witness. It is not a Boolean circuit lower bound, not a technology-independent mathematical invariant, and not evidence that a coordinate ordering persists on another FPGA family.")
$md.Add("")
$md.Add("The next cross-technology test should repeat the identical presentation family and observer definitions on a second target before any persistence claim is made.")

Set-Content -Path $MarkdownPath -Value $md -Encoding UTF8

Write-Host ""
Write-Host "== H19-LAB-01 PHYSICAL VISIBILITY ATLAS =="
$partitionRows | Format-Table -AutoSize
Write-Host ""
Write-Host ("Joint measured-profile partition: {0}" -f $jointText)
Write-Host ("D/P physical visibility vector: ({0})" -f ($visibilityBits -join ","))
Write-Host ""
Write-Host "Markdown:"
Write-Host $MarkdownPath
Write-Host "Partition CSV:"
Write-Host $PartitionCsvPath
