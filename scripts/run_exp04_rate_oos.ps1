param(
    [int]$ChunkSize = 500,
    [int]$MaxJobs = 4,
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$ZeroTable = Join-Path $Root "data\zeros\lmfdb_zeta_zeros_20001_40001.csv"
$OutDir = Join-Path $Root "data\derived\rh-sol-02-exp04-rate-oos"
$Cube = Join-Path $OutDir "rate_oos_20001_40000_q16_winding.npz"
$AnalysisOut = Join-Path $Root "papers\RH-SOL-02-SHIFT\analysis\exp04_rate_oos_summary.json"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

Write-Host "=== EXP-04 RATE-OOS ==="
Write-Host "Range      : loops 20001..40000"
Write-Host "Zero table : $ZeroTable"
Write-Host "Output cube: $Cube"
Write-Host "Geometry   : q=16 winding, dps=30, segments=60, boundary=1e-10"
Write-Host "Primary    : frozen M1 vs M2, no refit"

if (-not (Test-Path $ZeroTable)) {
    Write-Host "=== FETCH LMFDB ZEROS 20001..40001 ==="
    & $Python ".\scripts\fetch_lmfdb_zeros.py" --start 20001 --limit 20001 --out $ZeroTable
    if ($LASTEXITCODE -ne 0) { throw "zero-table fetch failed" }
}

$Chunks = @()
for ($Start = 20001; $Start -le 40000; $Start += $ChunkSize) {
    $Stop = [Math]::Min($Start + $ChunkSize - 1, 40000)
    $Chunk = Join-Path $OutDir ("chunk_{0:D5}_{1:D5}.npz" -f $Start, $Stop)
    $Chunks += $Chunk
}

$Pending = New-Object System.Collections.Generic.Queue[object]
for ($i = 0; $i -lt $Chunks.Count; $i++) {
    if (-not (Test-Path $Chunks[$i])) {
        $Start = 20001 + $i * $ChunkSize
        $Stop = [Math]::Min($Start + $ChunkSize - 1, 40000)
        $Pending.Enqueue([pscustomobject]@{ Start = $Start; Stop = $Stop; Out = $Chunks[$i] })
    }
}

Write-Host ("Chunks total={0} existing={1} pending={2}" -f $Chunks.Count, ($Chunks.Count - $Pending.Count), $Pending.Count)

$Running = @()
while ($Pending.Count -gt 0 -or $Running.Count -gt 0) {
    while ($Pending.Count -gt 0 -and $Running.Count -lt $MaxJobs) {
        $Task = $Pending.Dequeue()
        Write-Host ("START chunk {0}-{1}" -f $Task.Start, $Task.Stop)
        $PythonArguments = @(
            ".\scripts\exp01_build_chunk.py",
            "--start", [string]$Task.Start,
            "--stop", [string]$Task.Stop,
            "--zero-table", $ZeroTable,
            "--out", $Task.Out,
            "--dps", "30",
            "--segments", "60",
            "--q", "16",
            "--rules", "winding",
            "--boundary-tol", "1e-10"
        )
        $Job = Start-Job -ScriptBlock {
            param($PythonExe, $ArgsList, $WorkingDir)
            Set-Location $WorkingDir
            & $PythonExe @ArgsList
            if ($LASTEXITCODE -ne 0) { throw "chunk build failed with exit code $LASTEXITCODE" }
        } -ArgumentList $Python, $PythonArguments, $Root
        $Running += [pscustomobject]@{ Job = $Job; Task = $Task }
    }

    Start-Sleep -Seconds 1
    $Still = @()
    foreach ($Item in $Running) {
        if ($Item.Job.State -in @("Completed", "Failed", "Stopped")) {
            Receive-Job $Item.Job
            if ($Item.Job.State -ne "Completed") {
                $State = $Item.Job.State
                Remove-Job $Item.Job -Force
                throw ("chunk {0}-{1} ended in state {2}" -f $Item.Task.Start, $Item.Task.Stop, $State)
            }
            if (-not (Test-Path $Item.Task.Out)) {
                Remove-Job $Item.Job -Force
                throw ("chunk output missing: {0}" -f $Item.Task.Out)
            }
            Write-Host ("DONE  chunk {0}-{1}" -f $Item.Task.Start, $Item.Task.Stop)
            Remove-Job $Item.Job
        } else {
            $Still += $Item
        }
    }
    $Running = $Still
}

Write-Host "=== MERGE EXP-04 CHUNKS ==="
& $Python ".\scripts\exp01_merge_chunks.py" @Chunks --out $Cube
if ($LASTEXITCODE -ne 0) { throw "chunk merge failed" }

Write-Host "=== EXP-04 CUBE FINGERPRINT ==="
$Info = Get-Item $Cube
$Hash = Get-FileHash $Cube -Algorithm SHA256
Write-Host ("SIZE={0}" -f $Info.Length)
Write-Host ("SHA256={0}" -f $Hash.Hash.ToLowerInvariant())

Write-Host "=== FROZEN OOS SCORE ==="
& $Python ".\scripts\exp04_rate_oos_score.py" --dataset $Cube --out $AnalysisOut
if ($LASTEXITCODE -ne 0) { throw "EXP-04 OOS scoring failed" }

Write-Host "=== EXP-04 RATE-OOS COMPLETE ==="
Write-Host $Cube
Write-Host $AnalysisOut
