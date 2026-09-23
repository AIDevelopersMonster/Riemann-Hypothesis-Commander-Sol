$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path

foreach ($mode in @("scalar","quadratic")) {
  Write-Host ""
  Write-Host ("========== {0} ==========" -f $mode)
  & (Join-Path $Here "run_cyclonev_a7.ps1") -Mode $mode
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

& (Join-Path $Here "summarize_cyclonev_a7.ps1")
