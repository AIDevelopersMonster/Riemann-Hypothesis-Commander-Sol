param(
    [int]$ChunkSize = 500,
    [int]$MaxJobs = 4,
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if ($ChunkSize -le 0) { throw "ChunkSize must be positive" }
if ($MaxJobs -le 0) { throw "MaxJobs must be positive" }

$StartLoop = 10001
$StopLoop = 20000
$ZeroStart = 10001
$ZeroLimit = 10001
$ZeroTable = Join-Path $RepoRoot "data\zeros\lmfdb_zeta_zeros_10001_20001.csv"
$OutDir = Join-Path $RepoRoot "data\derived\rh-sol-02-exp01-holdout"
$Merged = Join-Path $OutDir "holdout_10001_20000.npz"
$AnalysisDir = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\analysis"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
New-Item -ItemType Directory -Force -Path $AnalysisDir | Out-Null

Write-Host "=== HOLDOUT FREEZE CHECK ==="
$Freeze = Join-Path $RepoRoot "papers\RH-SOL-02-SHIFT\CALIBRATION_FREEZE.md"
if (-not (Test-Path $Freeze)) { throw "Missing calibration freeze document: $Freeze" }
Write-Host $Freeze

Write-Host "=== PYTHON PREFLIGHT ==="
& $Python -c "import sys; print(sys.executable); import mpmath, numpy, scipy, shapely; print('mpmath=' + mpmath.__version__); print('numpy=' + numpy.__version__); print('scipy=' + scipy.__version__); print('shapely=' + shapely.__version__)"
if ($LASTEXITCODE -ne 0) { throw "Python dependency preflight failed" }

if (-not (Test-Path $ZeroTable)) {
    Write-Host "=== FETCH LMFDB ZEROS 10001..20001 ==="
    & $Python "scripts\fetch_lmfdb_zeros.py" `
        --start $ZeroStart `
        --limit $ZeroLimit `
        --out $ZeroTable
    if ($LASTEXITCODE -ne 0) { throw "holdout zero-table acquisition failed" }
} else {
    Write-Host "=== REUSE EXISTING HOLDOUT ZERO TABLE ==="
    Write-Host $ZeroTable
}

$Ranges = @()
for ($Start = $StartLoop; $Start -le $StopLoop; $Start += $ChunkSize) {
    $Stop = [Math]::Min($StopLoop, $Start + $ChunkSize - 1)
    $Name = "chunk_{0:D5}_{1:D5}.npz" -f $Start, $Stop
    $Path = Join-Path $OutDir $Name
    $Ranges += [PSCustomObject]@{ Start = $Start; Stop = $Stop; Path = $Path }
}

$Pending = @($Ranges | Where-Object { -not (Test-Path $_.Path) })
Write-Host ("Holdout chunks total: {0}; already present: {1}; pending: {2}" -f $Ranges.Count, ($Ranges.Count - $Pending.Count), $Pending.Count)

function Complete-OneJob {
    param([System.Management.Automation.Job]$Job)
    Receive-Job -Job $Job -ErrorAction Continue
    if ($Job.State -ne 'Completed') {
        $Reason = $null
        if ($Job.ChildJobs.Count -gt 0) { $Reason = $Job.ChildJobs[0].JobStateInfo.Reason }
        throw "Holdout chunk job failed: $($Job.Name). Reason: $Reason"
    }
    $ExpectedPath = [string]$Job.ExpectedPath
    if (-not (Test-Path $ExpectedPath)) { throw "Expected holdout chunk missing: $ExpectedPath" }
    Write-Host ("DONE {0} -> {1} bytes" -f $Job.Name, (Get-Item $ExpectedPath).Length)
}

$Jobs = @()
foreach ($Range in $Pending) {
    while ($Jobs.Count -ge $MaxJobs) {
        $Done = Wait-Job -Job $Jobs -Any
        Complete-OneJob -Job $Done
        Remove-Job $Done
        $Jobs = @($Jobs | Where-Object { $_.Id -ne $Done.Id })
    }

    $PythonArguments = @(
        "scripts\exp01_build_chunk.py",
        "--start", [string]$Range.Start,
        "--stop", [string]$Range.Stop,
        "--zero-table", [string]$ZeroTable,
        "--out", [string]$Range.Path,
        "--dps", "30",
        "--segments", "60",
        "--q", "8", "16", "32",
        "--rules", "winding", "even-odd",
        "--boundary-tol", "1e-10"
    )

    $JobName = "HOLDOUT_{0:D5}_{1:D5}" -f $Range.Start, $Range.Stop
    $Job = Start-Job -Name $JobName -ScriptBlock {
        param($WorkingDirectory, $PythonExe, $PythonArgumentList)
        Set-Location $WorkingDirectory
        & $PythonExe @PythonArgumentList
        $ExitCode = $LASTEXITCODE
        if ($ExitCode -ne 0) { throw "python exit code $ExitCode" }
    } -ArgumentList $RepoRoot, $Python, $PythonArguments

    $Job | Add-Member -NotePropertyName ExpectedPath -NotePropertyValue ([string]$Range.Path)
    $Jobs += $Job
    Write-Host ("START {0}" -f $JobName)
}

while ($Jobs.Count -gt 0) {
    $Done = Wait-Job -Job $Jobs -Any
    Complete-OneJob -Job $Done
    Remove-Job $Done
    $Jobs = @($Jobs | Where-Object { $_.Id -ne $Done.Id })
}

$Missing = @($Ranges | Where-Object { -not (Test-Path $_.Path) })
if ($Missing.Count -gt 0) { throw "Missing holdout chunk files after generation: $($Missing.Count)" }

Write-Host "=== MERGE HOLDOUT CHUNKS ==="
$ChunkPaths = @($Ranges | ForEach-Object { $_.Path })
& $Python "scripts\exp01_merge_chunks.py" @ChunkPaths --out $Merged
if ($LASTEXITCODE -ne 0) { throw "holdout chunk merge failed" }
if (-not (Test-Path $Merged)) { throw "holdout merge output missing: $Merged" }

Write-Host "=== HOLDOUT CUBE FINGERPRINT ==="
$Hash = (Get-FileHash $Merged -Algorithm SHA256).Hash.ToLower()
$Size = (Get-Item $Merged).Length
Write-Host ("SIZE={0}" -f $Size)
Write-Host ("SHA256={0}" -f $Hash)

Write-Host "=== PRIMARY HOLDOUT q=16 WINDING MAP ==="
& $Python "scripts\exp01_analyze_shift_map.py" `
    --dataset $Merged `
    --rule winding `
    --q 16 `
    --B 20000 `
    --out (Join-Path $AnalysisDir "exp01_holdout_shift_map_winding_q16_midpoint.csv")
if ($LASTEXITCODE -ne 0) { throw "primary holdout shift-map analysis failed" }

Write-Host "=== PRIMARY HOLDOUT ZERO-MODE DECOMPOSITION ==="
& $Python "scripts\exp01_decompose_zero_mode.py" `
    --dataset $Merged `
    --rule winding `
    --q 16 `
    --B 20000 `
    --out-prefix (Join-Path $AnalysisDir "exp01_holdout_zero_mode_winding_q16_midpoint")
if ($LASTEXITCODE -ne 0) { throw "primary holdout zero-mode analysis failed" }

Write-Host "=== HOLDOUT RESOLUTION/FILL-RULE CONTROLS ==="
& $Python "scripts\exp01_control_suite.py" `
    --dataset $Merged `
    --q 8 16 32 `
    --rules winding even-odd `
    --B 20000 `
    --expected-start 10001 `
    --expected-stop 20000 `
    --out-prefix (Join-Path $AnalysisDir "exp01_holdout_control_suite_midpoint")
if ($LASTEXITCODE -ne 0) { throw "holdout control suite failed" }

Write-Host "=== EXP-01 INDEPENDENT HOLDOUT COMPLETE ==="
Write-Host $Merged
Write-Host (Join-Path $AnalysisDir "exp01_holdout_shift_map_winding_q16_midpoint.json")
Write-Host (Join-Path $AnalysisDir "exp01_holdout_zero_mode_winding_q16_midpoint.json")
Write-Host (Join-Path $AnalysisDir "exp01_holdout_control_suite_midpoint.json")
