param(
    [ValidateSet("calibration", "holdout", "both")]
    [string]$Stage = "both",
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Cal1 = Join-Path $Root "data\derived\rh-sol-02-exp01\calibration_1_10000.npz"
$Cal2 = Join-Path $Root "data\derived\rh-sol-02-exp01-holdout\holdout_10001_20000.npz"
$Hold = Join-Path $Root "data\derived\rh-sol-02-exp04-rate-oos\rate_oos_20001_40000_q16_winding.npz"
$AnalysisDir = Join-Path $Root "papers\RH-SOL-04-FIREWALL\analysis"
New-Item -ItemType Directory -Force -Path $AnalysisDir | Out-Null

function Run-FirewallRange {
    param(
        [string[]]$Datasets,
        [int]$Start,
        [int]$Stop,
        [string]$Name
    )

    foreach ($Path in $Datasets) {
        if (-not (Test-Path $Path)) { throw "Missing required dataset: $Path" }
    }

    $Out = Join-Path $AnalysisDir ("firewall_{0}.json" -f $Name)

    Write-Host "=== RH-SOL-04 FIREWALL ==="
    Write-Host ("Range      : loops {0}..{1}" -f $Start, $Stop)
    Write-Host "Observable : winding filled area"
    Write-Host "Time       : actual zero-pair midpoint"
    Write-Host "Test 01    : independent within-block circular offsets"
    Write-Host "Test 02    : whole-block geometry reassignment"
    Write-Host "Targets    : exact log(m), primary m=2..13, sensitivity m=2..11"
    Write-Host "Surrogates : B=5000 per family"

    & $Python ".\scripts\firewall_assignment_surrogates.py" @Datasets `
        --start $Start `
        --stop $Stop `
        --out $Out `
        --block-size 1000 `
        --B 5000 `
        --seed-circular 20260825 `
        --seed-block 20260826

    if ($LASTEXITCODE -ne 0) { throw "FIREWALL failed for $Name" }
    Write-Host ("COMPLETE   : {0}" -f $Out)
}

if ($Stage -in @("calibration", "both")) {
    Run-FirewallRange -Datasets @($Cal1, $Cal2) -Start 1 -Stop 20000 -Name "calibration_1_20000"
}

if ($Stage -in @("holdout", "both")) {
    Run-FirewallRange -Datasets @($Hold) -Start 20001 -Stop 40000 -Name "holdout_20001_40000"
}

Write-Host "=== RH-SOL-04 FIREWALL PRIMARY RUN COMPLETE ==="
