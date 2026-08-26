param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$HeightJson = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\analysis\exp02_height_blocks_1000.json"
$Out = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\analysis\exp03_rate_summary.json"

if (-not (Test-Path $HeightJson)) {
    throw "Missing EXP-02 HEIGHT JSON: $HeightJson"
}

Write-Host "=== EXP-03 RATE ==="
Write-Host ("Input : {0}" -f $HeightJson)
Write-Host ("Output: {0}" -f $Out)

& $Python "scripts\exp03_rate_analysis.py" `
    --height-json $HeightJson `
    --out $Out

if ($LASTEXITCODE -ne 0) {
    throw "EXP-03 RATE analysis failed"
}

Write-Host "=== EXP-03 RATE COMPLETE ==="
Write-Host $Out
