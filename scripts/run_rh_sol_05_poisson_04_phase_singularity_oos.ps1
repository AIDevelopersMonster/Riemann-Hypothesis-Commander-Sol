param(
    [string]$Python = "python",
    [int]$B = 2000
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$ZeroTable = Join-Path $Root "data\zeros\lmfdb_zeta_zeros_20001_40001.csv"
$ChunkDir = Join-Path $Root "data\derived\rh-sol-05-poisson-04-phase-singularity-oos\chunks"
$Merged = Join-Path $Root "data\derived\rh-sol-05-poisson-04-phase-singularity-oos\oos_20001_40000_q16_q32.npz"
$Out = Join-Path $Root "papers\RH-SOL-05-POISSON\analysis\poisson_04_phase_singularity_oos_20001_40000.json"

if (-not (Test-Path $ZeroTable)) {
    throw "Missing zero table: $ZeroTable"
}

New-Item -ItemType Directory -Force -Path $ChunkDir | Out-Null

Write-Host "=== RH-SOL-05 POISSON-04 / PHASE-SINGULARITY OOS ==="
Write-Host "Identity     : POISSON-04_PHASE_SINGULARITY_OOS"
Write-Host "Fresh range  : loops 20001..40000"
Write-Host "Tensor       : winding-only q16/q32"
Write-Host "Strata       : bottom10 / middle80 / top10 by min |G32|"
Write-Host "Primary      : bottom10 > top10 > middle80"
Write-Host "Null         : independent target jitter +/-0.20, B=$B"
Write-Host "Output       : $Out"

if (-not (Test-Path $Merged)) {
    Write-Host "Fresh OOS tensor not found; building resumable 1000-loop chunks."

    for ($Start = 20001; $Start -le 39001; $Start += 1000) {
        $Stop = $Start + 999
        $Chunk = Join-Path $ChunkDir ("chunk_{0}_{1}.npz" -f $Start, $Stop)
        if (Test-Path $Chunk) {
            Write-Host "SKIP existing $Chunk"
            continue
        }

        Write-Host "BUILD $Start..$Stop"
        & $Python ".\scripts\exp01_build_chunk.py" `
            --start $Start `
            --stop $Stop `
            --zero-table $ZeroTable `
            --out $Chunk `
            --dps 30 `
            --segments 60 `
            --q 16 32 `
            --rules winding `
            --boundary-tol 1e-10

        if ($LASTEXITCODE -ne 0) {
            throw "OOS chunk build failed for $Start..$Stop"
        }
    }

    $Chunks = Get-ChildItem -Path $ChunkDir -Filter "chunk_*.npz" | Sort-Object Name | ForEach-Object { $_.FullName }
    if ($Chunks.Count -ne 20) {
        throw "Expected 20 OOS chunks, found $($Chunks.Count)"
    }

    & $Python ".\scripts\exp01_merge_chunks.py" @Chunks --out $Merged
    if ($LASTEXITCODE -ne 0) {
        throw "OOS chunk merge failed"
    }
}
else {
    Write-Host "Using existing fresh OOS tensor: $Merged"
}

& $Python ".\scripts\rh_sol_05_poisson_04_phase_singularity_oos.py" `
    --data $Merged `
    --out $Out `
    --B $B

if ($LASTEXITCODE -ne 0) {
    throw "POISSON-04_PHASE_SINGULARITY_OOS failed"
}

Write-Host "=== POISSON-04_PHASE_SINGULARITY_OOS COMPLETE ==="
Write-Host $Out
