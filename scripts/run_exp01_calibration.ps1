param(
    [int]$ChunkSize = 500,
    [int]$MaxJobs = 4,
    [string]$Python = "python",
    [switch]$Adaptive
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if ($ChunkSize -le 0) { throw "ChunkSize must be positive" }
if ($MaxJobs -le 0) { throw "MaxJobs must be positive" }

Write-Host "=== PYTHON PREFLIGHT ==="
& $Python -c "import sys; print(sys.executable); import mpmath, numpy, scipy, shapely; print('mpmath=' + mpmath.__version__); print('numpy=' + numpy.__version__); print('scipy=' + scipy.__version__); print('shapely=' + shapely.__version__)"
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Required packages are missing from the selected Python environment."
    Write-Host "Install them with:"
    Write-Host ("  {0} -m pip install -r requirements.txt" -f $Python)
    Write-Host "Then rerun this script."
    throw "Python dependency preflight failed"
}

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
} else {
    Write-Host "=== REUSE EXISTING ZERO TABLE ==="
    Write-Host $ZeroTable
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

function Complete-OneJob {
    param([System.Management.Automation.Job]$Job)

    Receive-Job -Job $Job -ErrorAction Continue

    if ($Job.State -ne 'Completed') {
        $Reason = $null
        if ($Job.ChildJobs.Count -gt 0) {
            $Reason = $Job.ChildJobs[0].JobStateInfo.Reason
        }
        throw "EXP-01 chunk job failed: $($Job.Name). Reason: $Reason"
    }

    $ExpectedPath = [string]$Job.ExpectedPath
    if (-not (Test-Path $ExpectedPath)) {
        throw "EXP-01 job completed but expected chunk was not created: $ExpectedPath"
    }

    $Size = (Get-Item $ExpectedPath).Length
    Write-Host ("DONE {0} -> {1} bytes" -f $Job.Name, $Size)
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
        "--out", [string]$Range.Path
    )
    if ($Adaptive) { $PythonArguments += "--adaptive" }

    $JobName = "EXP01_{0:D5}_{1:D5}" -f $Range.Start, $Range.Stop
    $Job = Start-Job -Name $JobName -ScriptBlock {
        param($WorkingDirectory, $PythonExe, $PythonArgumentList)
        Set-Location $WorkingDirectory
        & $PythonExe @PythonArgumentList
        $ExitCode = $LASTEXITCODE
        if ($ExitCode -ne 0) {
            throw "python exit code $ExitCode"
        }
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
if ($Missing.Count -gt 0) {
    Write-Host "Missing chunks:"
    $Missing | ForEach-Object { Write-Host ("  {0}-{1}: {2}" -f $_.Start, $_.Stop, $_.Path) }
    throw "Missing chunk files after generation: $($Missing.Count)"
}

Write-Host "=== MERGE CHUNKS ==="
$ChunkPaths = @($Ranges | ForEach-Object { $_.Path })
$Merged = Join-Path $OutDir "calibration_1_10000.npz"
& $Python "scripts\exp01_merge_chunks.py" @ChunkPaths --out $Merged
if ($LASTEXITCODE -ne 0) { throw "chunk merge failed" }
if (-not (Test-Path $Merged)) { throw "merge reported success but output is missing: $Merged" }

Write-Host "=== EXP-01 CALIBRATION CUBE READY ==="
Write-Host $Merged
Write-Host "Next: run scripts\exp01_analyze_shift_map.py for q=16 winding."
