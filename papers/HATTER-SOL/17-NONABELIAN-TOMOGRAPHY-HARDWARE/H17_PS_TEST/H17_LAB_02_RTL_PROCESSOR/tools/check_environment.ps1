$ErrorActionPreference = "Stop"

Write-Host "H17-LAB-02 Windows environment check"
Write-Host ""

$failed = $false

function Check-Command([string]$Name, [string[]]$Args) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $cmd) {
        Write-Host "[FAIL] $Name not found in PATH"
        return $false
    }

    Write-Host "[ OK ] $Name -> $($cmd.Source)"
    try {
        & $Name @Args 2>&1 | Select-Object -First 4 | ForEach-Object {
            Write-Host "      $_"
        }
    }
    catch {
        Write-Host "      version probe failed: $($_.Exception.Message)"
    }
    return $true
}

if (-not (Check-Command "git" @("--version"))) { $failed = $true }
if (-not (Check-Command "py" @("-3","--version"))) { $failed = $true }
if (-not (Check-Command "iverilog" @("-V"))) { $failed = $true }
if (-not (Check-Command "vvp" @("-V"))) { $failed = $true }

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$Ref = Join-Path $Lab "..\H17_LAB_COMPLETE_clean"

$required = @(
    (Join-Path $Lab "rtl\h17_lab02_core.sv"),
    (Join-Path $Lab "tb\tb_h17_lab02_vectors.sv"),
    (Join-Path $Ref "vectors\quick.txt"),
    (Join-Path $Ref "vectors\full.txt")
)

foreach ($p in $required) {
    if (Test-Path $p) {
        Write-Host "[ OK ] file: $p"
    } else {
        Write-Host "[FAIL] missing: $p"
        $failed = $true
    }
}

if ($failed) {
    throw "H17 Windows environment check FAILED"
}

Write-Host ""
Write-Host "PASS H17 Windows environment"
