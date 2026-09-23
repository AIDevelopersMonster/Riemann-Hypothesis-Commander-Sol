$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$Tcl = Join-Path $Lab "quartus13_stratixv_probe.tcl"
$Out = Join-Path $Lab "quartus13_stratixv_probe.txt"

$Quartus = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"
if (!(Test-Path $Quartus)) { throw "Quartus II 13.1 not found at $Quartus" }

Write-Host "== Quartus II 13.1 Stratix V local-device probe =="
& $Quartus --version

& $Quartus -t $Tcl 2>&1 | Tee-Object -FilePath $Out
$rc = $LASTEXITCODE

Write-Host ""
Write-Host "Probe report:"
Write-Host $Out

if ($rc -eq 2) {
    Write-Host "RESULT: Stratix V device family is not installed in this Quartus instance."
    exit 2
}
if ($rc -ne 0) {
    throw "Quartus Stratix V probe failed with exit code $rc"
}

Write-Host "RESULT: Stratix V family database is installed. Use the reported exact part names for the benchmark target."
