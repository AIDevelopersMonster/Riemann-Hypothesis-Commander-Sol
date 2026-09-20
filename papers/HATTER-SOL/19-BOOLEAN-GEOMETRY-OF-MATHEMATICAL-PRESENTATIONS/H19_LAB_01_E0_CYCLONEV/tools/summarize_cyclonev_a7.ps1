$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$Modes = @("direct12","prefix19","nielsen12")
$rows = @()

function First-MatchValue([string]$Path,[string]$Pattern,[string]$Group="v") {
  if (!(Test-Path $Path)) { return $null }
  foreach ($line in Get-Content $Path) {
    $m = [regex]::Match($line,$Pattern)
    if ($m.Success) { return $m.Groups[$Group].Value }
  }
  return $null
}

foreach ($mode in $Modes) {
  $QDir = Join-Path $Lab ("quartus13_cyclonev_a7\" + $mode)
  $Project = "h19_" + $mode + "_cv_a7"
  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  $Sta = Join-Path $QDir "output_files\$Project.sta.rpt"
  $Worst = Join-Path $QDir "worst_path_full.rpt"

  $fitStatus = if (Test-Path $Fit) {
    if (Select-String -Path $Fit -Pattern "Fitter was successful|Fitter successful" -Quiet) { "FIT" }
    elseif (Select-String -Path $Fit -Pattern "Can't fit design|Design contains.*However, the device contains" -Quiet) { "NOFIT" }
    else { "UNKNOWN" }
  } else { "MISSING" }

  $alm = First-MatchValue $Fit 'Logic utilization \(in ALMs\)\s*;\s*(?<v>[\d,]+)\s*/'
  if (!$alm) { $alm = First-MatchValue $Fit 'Total ALMs\s*;\s*(?<v>[\d,]+)\s*/' }

  $regs = First-MatchValue $Fit 'Total registers\s*;\s*(?<v>[\d,]+)'
  $dsp = First-MatchValue $Fit 'Total DSP Blocks\s*;\s*(?<v>[\d,]+)\s*/'
  if (!$dsp) { $dsp = First-MatchValue $Fit 'DSP block 18-bit elements\s*;\s*(?<v>[\d,]+)\s*/' }

  $fmax = First-MatchValue $Sta '(?<v>\d+(?:\.\d+)?)\s*MHz.*clk'
  if (!$fmax) { $fmax = First-MatchValue $Sta 'clk\s*;\s*(?<v>\d+(?:\.\d+)?)\s*MHz' }

  $delay = First-MatchValue $Worst 'Data Delay\s*:\s*(?<v>\d+(?:\.\d+)?)\s*ns'
  $levels = First-MatchValue $Worst 'Number of Logic Levels\s*:\s*(?<v>\d+)'
  $cell = First-MatchValue $Worst 'Data Cell Delay\s*:\s*(?<v>\d+(?:\.\d+)?)\s*ns'
  $route = First-MatchValue $Worst 'Data Routing Delay\s*:\s*(?<v>\d+(?:\.\d+)?)\s*ns'

  $rows += [pscustomobject]@{
    Mode = $mode
    Fit = $fitStatus
    ALM = $alm
    Registers = $regs
    DSP = $dsp
    Fmax_MHz = $fmax
    DataDelay_ns = $delay
    LogicLevels = $levels
    Cell_ns = $cell
    Routing_ns = $route
  }
}

Write-Host "== H19-LAB-01 MATCHED CYCLONE V SUMMARY =="
$rows | Format-Table -AutoSize

$csv = Join-Path $Lab "H19_LAB01_CYCLONEV_SUMMARY.csv"
$rows | Export-Csv -NoTypeInformation -Encoding UTF8 $csv
Write-Host ""
Write-Host "CSV:"
Write-Host $csv
