$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$rows = @()

function First-MatchValue([string]$Path,[string]$Pattern,[string]$Group="v") {
  if (!(Test-Path $Path)) { return $null }
  foreach ($line in Get-Content $Path) {
    $m = [regex]::Match($line,$Pattern)
    if ($m.Success) { return $m.Groups[$Group].Value }
  }
  return $null
}

foreach ($mode in @("scalar","quadratic")) {
  $QDir = Join-Path $Lab ("quartus13_cyclonev_a7\" + $mode)
  $Project = "h21_b0_" + $mode + "_cv_a7"
  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  $Sta = Join-Path $QDir "output_files\$Project.sta.rpt"

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
  $fmax = First-MatchValue $Sta ';\s*(?<v>\d+(?:\.\d+)?)\s*MHz\s*;\s*\d+(?:\.\d+)?\s*MHz\s*;\s*clk\s*;'

  $rows += [pscustomobject]@{
    Mode = $mode
    Fit = $fitStatus
    ALM = $alm
    Registers = $regs
    DSP = $dsp
    Fmax_MHz = $fmax
  }
}

Write-Host "== H21-LAB-28 CYCLONE V SUMMARY =="
$rows | Format-Table -AutoSize

$csv = Join-Path $Lab "H21_LAB28_CYCLONEV_SUMMARY.csv"
$rows | Export-Csv -NoTypeInformation -Encoding UTF8 $csv

$scalar = $rows | Where-Object { $_.Mode -eq "scalar" }
$quad = $rows | Where-Object { $_.Mode -eq "quadratic" }

if ($scalar.ALM -and $quad.ALM) {
  $sa = [double](($scalar.ALM -replace ',',''))
  $qa = [double](($quad.ALM -replace ',',''))
  Write-Host ("ALM ratio quadratic/scalar: {0:N4}x" -f ($qa/$sa))
}
if ($scalar.Fmax_MHz -and $quad.Fmax_MHz) {
  $sf = [double]$scalar.Fmax_MHz
  $qf = [double]$quad.Fmax_MHz
  Write-Host ("Fmax ratio scalar/quadratic: {0:N4}x" -f ($sf/$qf))
}

Write-Host ("CSV: {0}" -f $csv)
