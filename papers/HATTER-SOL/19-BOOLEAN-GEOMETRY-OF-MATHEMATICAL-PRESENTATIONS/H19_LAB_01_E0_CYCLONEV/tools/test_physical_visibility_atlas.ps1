$ErrorActionPreference = "Stop"

$Tools = $PSScriptRoot
$Lab = Resolve-Path (Join-Path $Tools "..")
$Tmp = Join-Path $Lab "_atlas_selftest"

if (Test-Path $Tmp) {
  Remove-Item -Recurse -Force $Tmp
}
New-Item -ItemType Directory -Force $Tmp | Out-Null

$csv = Join-Path $Tmp "fixture.csv"
$md = Join-Path $Tmp "atlas.md"
$out = Join-Path $Tmp "partitions.csv"

@"
Mode,Fit,ALM,Registers,DSP,Fmax_MHz,DataDelay_ns,LogicLevels,Cell_ns,Routing_ns
direct12,FIT,1000,69,40,30.00,33.000,30,12.000,21.000
prefix19,FIT,1000,69,40,30.10,32.900,30,12.100,20.800
nielsen12,FIT,1200,69,48,28.00,35.000,34,13.000,22.000
"@ | Set-Content -Path $csv -Encoding ascii

& (Join-Path $Tools "analyze_physical_visibility_atlas.ps1") -CsvPath $csv -MarkdownPath $md -PartitionCsvPath $out

if ($LASTEXITCODE -ne 0) {
  throw "atlas analyzer returned nonzero exit code"
}

if (!(Test-Path $md)) { throw "missing atlas markdown" }
if (!(Test-Path $out)) { throw "missing partition csv" }

$rows = @(Import-Csv $out)

function Need([string]$observer,[string]$partition,[string]$dp) {
  $r = $rows | Where-Object { $_.Observer -eq $observer } | Select-Object -First 1
  if (!$r) { throw "missing observer row: $observer" }
  if ($r.Partition -ne $partition) {
    throw "partition mismatch for $observer: got $($r.Partition), expected $partition"
  }
  if ([string]$r.DirectPrefixVisible -ne $dp) {
    throw "D/P visibility mismatch for $observer"
  }
}

Need "ALM" "{{D,P},{N}}" "0"
Need "Registers" "{{D,P,N}}" "0"
Need "DSP" "{{D,P},{N}}" "0"
Need "Fmax_MHz" "{{D},{P},{N}}" "1"
Need "DataDelay_ns" "{{D},{P},{N}}" "1"
Need "LogicLevels" "{{D,P},{N}}" "0"
Need "Cell_ns" "{{D},{P},{N}}" "1"
Need "Routing_ns" "{{D},{P},{N}}" "1"

$jointLine = Select-String -Path $md -Pattern "Joint-profile partition: \{\{D\},\{P\},\{N\}\}" -Quiet
if (!$jointLine) {
  throw "joint profile should be discrete in fixture"
}

Write-Host "PASS: H19 physical visibility atlas analyzer self-test"

Remove-Item -Recurse -Force $Tmp
