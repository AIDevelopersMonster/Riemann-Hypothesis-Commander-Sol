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

function Get-FirstDataPathStats([string]$Path) {
  $result = @{
    DataDelay = $null
    LogicLevels = $null
    CellDelay = $null
    RoutingDelay = $null
  }
  if (!(Test-Path $Path)) { return $result }

  $inFirstPath = $false
  $inDataSection = $false

  foreach ($line in Get-Content $Path) {
    if (!$inFirstPath -and $line -match '^Path #1:') {
      $inFirstPath = $true
      continue
    }
    if (!$inFirstPath) { continue }

    if (!$result.DataDelay) {
      $m = [regex]::Match($line,';\s*Data Delay\s*;\s*(?<v>\d+(?:\.\d+)?)\s*;')
      if ($m.Success) { $result.DataDelay = $m.Groups["v"].Value }
    }

    if (!$result.LogicLevels) {
      $m = [regex]::Match($line,';\s*Number of Logic Levels\s*;\s*;\s*(?<v>\d+)\s*;')
      if ($m.Success) { $result.LogicLevels = $m.Groups["v"].Value }
    }

    if ($line -match '^;\s+Data\s+;') {
      $inDataSection = $true
      continue
    }

    if ($inDataSection -and $line -match '^;\s+Required Path\s+;') {
      break
    }

    if ($inDataSection -and !$result.CellDelay) {
      $m = [regex]::Match($line,';\s*Cell\s*;\s*;\s*\d+\s*;\s*(?<v>\d+(?:\.\d+)?)\s*;')
      if ($m.Success) { $result.CellDelay = $m.Groups["v"].Value }
    }

    if ($inDataSection -and !$result.RoutingDelay) {
      $m = [regex]::Match($line,';\s*Routing Element\s*;\s*;\s*\d+\s*;\s*(?<v>\d+(?:\.\d+)?)\s*;')
      if ($m.Success) { $result.RoutingDelay = $m.Groups["v"].Value }
    }
  }

  return $result
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

  # Match the first actual Fmax Summary row. Do not match the 100 MHz
  # create_clock/clock-settings line.
  $fmax = First-MatchValue $Sta ';\s*(?<v>\d+(?:\.\d+)?)\s*MHz\s*;\s*\d+(?:\.\d+)?\s*MHz\s*;\s*clk\s*;'

  $pathStats = Get-FirstDataPathStats $Worst
  $delay = $pathStats.DataDelay
  $levels = $pathStats.LogicLevels
  $cell = $pathStats.CellDelay
  $route = $pathStats.RoutingDelay

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
