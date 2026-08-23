param(
    [int]$ChunkSize = 500,
    [int]$MaxJobs = 4,
    [string]$Python = "python",
    [switch]$Adaptive
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$ZeroTable = Join-Path $RepoRoot "data\zeros\lmfdb_zeta_zeros_1_10001.csv"
$OutDir = Join-Path $RepoRoot "data\derived\rh-sol-02-exp01"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

if (-not (Test-Path $ZeroTable)) {
    Write-Host "=== FETCH LMFDB ZEROS 1..10001 ==="
    & $Python "scripts\fetch_lmfdb_zeros.py" `
        --start 1 `
        --limit 10001 `
        --out $ZeroTable
    if ($LASTEXITCODE -ne 0) { throw "zero-table acquisition failed" }
}

$Ranges = @()
for ($Start = 1; $Start -le 10000; $Start += $ChunkSize) {
    $Stop = [Math]::Min(10000, $Start + $ChunkSize - 1)
    $Name = "chunk_{0:D5}_{1:D5}.npz" -f $Start, $Stop
    $Path = Join-Path $OutDir $Name
    $Ranges += [PSCustomObject]@{ Start = $Start; Stop = $Stop; Path = $Path }
}

$Pending = @($Ranges | Where-Object { -not (Test-Path $_.Path) })
Write-Host ("Chunks total: {0}; already present: {1}; pending: {2}" -f $Ranges.Count, ($Ranges.Count - $Pending.Count), $Pending.Count)

$Jobs = @()
foreach ($Range in $Pending) {
    while (($Jobs | Where-Object { $_.State -eq 'Running' }).Count -ge $MaxJobs) {
        $Done = Wait-Job -Job $Jobs -Any
        Receive-Job $Done
        if ($Done.State -ne 'Completed') {
            throw "EXP-01 chunk job failed: $($Done.Name)"
        }
        Remove-Job $Done
        $Jobs = @($Jobs | Where-Object { $_.Id -ne $Done.Id })
    }

    $Args = @(
        "scripts\exp01_build_chunk.py",
        "--start", $Range.Start,
        "--stop", $Range.Stop,
        "--zero-table", $ZeroTable,
        "--out", $Range.Path
    )
    if ($Adaptive) { $Args += "--adaptive" }

    $JobName = "EXP01_{0:D5}_{1:D5}" -f $Range.Start, $Range.Stop
    $Jobs += Start-Job -Name $JobName -ScriptBlock {
        param($RepoRoot, $Python, $Args)
        Set-Location $RepoRoot
        & $Python @Args
        if ($LASTEXITCODE -ne 0) { throw "python exit code $LASTEXITCODE" }
    } -ArgumentList $RepoRoot, $Python, $Args
}

while ($Jobs.Count -gt 0) {
    $Done = Wait-Job -Job $Jobs -Any
    Receive-Job $Done
    if ($Done.State -ne 'Completed') {
        throw "EXP-01 chunk job failed: $($Done.Name)"
    }
    Remove-Job $Done
    $Jobs = @($Jobs | Where-Object { $_.Id -ne $Done.Id })
}

$Missing = @($Ranges | Where-Object { -not (Test-Path $_.Path) })
if ($Missing.Count -gt 0) {
    throw "Missing chunk files after generation: $($Missing.Count)"
}

Write-Host "=== MERGE CHUNKS ==="
$ChunkPaths = @($Ranges | ForEach-Object { $_.Path })
$Merged = Join-Path $OutDir "calibration_1_10000.npz"
& $Python "scripts\exp01_merge_chunks.py" @ChunkPaths --out $Merged
if ($LASTEXITCODE -ne 0) { throw "chunk merge failed" }

Write-Host "=== EXP-01 CALIBRATION CUBE READY ==="
Write-Host $Merged
Write-Host "Next: run scripts\exp01_analyze_shift_map.py for q=16 winding."
