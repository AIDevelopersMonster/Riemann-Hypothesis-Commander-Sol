$ErrorActionPreference = "Stop"
$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$Tcl = Join-Path $Lab "quartus13_cyclonev_probe.tcl"
$Out = Join-Path $Lab "quartus13_cyclonev_probe.txt"
$Quartus = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"

if (!(Test-Path $Quartus)) { throw "Quartus II 13.1 not found at $Quartus" }

Write-Host "== Quartus II 13.1 Cyclone V local-device probe =="
& $Quartus --version
& $Quartus -t $Tcl 2>&1 | Tee-Object -FilePath $Out
$rc = $LASTEXITCODE

Write-Host ""
Write-Host "Probe report:"
Write-Host $Out

if ($rc -eq 2) {
    Write-Host "RESULT: Cyclone V device files are not installed."
    Write-Host "Official Quartus II 13.1 Web package: cyclonev-13.1.0.162.qdz"
    exit 2
}
if ($rc -ne 0) { throw "Cyclone V probe failed with exit code $rc" }

Write-Host "RESULT: Cyclone V database is installed."
Write-Host "Use an exact reported 5CEA7 part for the H17 benchmark."
