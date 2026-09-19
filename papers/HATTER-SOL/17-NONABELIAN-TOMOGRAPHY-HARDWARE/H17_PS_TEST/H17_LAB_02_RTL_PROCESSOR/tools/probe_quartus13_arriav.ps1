$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$Tcl = Join-Path $Lab "quartus13_arriav_probe.tcl"
$Out = Join-Path $Lab "quartus13_arriav_probe.txt"
$Quartus = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"

if (!(Test-Path $Quartus)) {
    throw "Quartus II 13.1 not found at $Quartus"
}

if (!(Test-Path $Tcl)) {
    throw "Arria V probe Tcl not found at $Tcl"
}

Write-Host "== Quartus II 13.1 Arria V local-device probe =="
& $Quartus --version

& $Quartus -t $Tcl 2>&1 | Tee-Object -FilePath $Out
$rc = $LASTEXITCODE

Write-Host ""
Write-Host "Probe report:"
Write-Host $Out

if ($rc -eq 2) {
    Write-Host "RESULT: Arria V device family is not installed in this Quartus instance."
    exit 2
}

if ($rc -ne 0) {
    throw "Quartus Arria V probe failed with exit code $rc"
}

Write-Host "RESULT: Arria V family database is installed."
Write-Host "Use one of the exact reported commercial part numbers for the H17 benchmark."
