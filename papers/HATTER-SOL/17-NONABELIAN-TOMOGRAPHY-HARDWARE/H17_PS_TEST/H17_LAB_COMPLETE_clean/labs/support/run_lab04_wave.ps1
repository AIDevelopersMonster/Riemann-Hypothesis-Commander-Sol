$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$Build = Join-Path $Root "build"

New-Item -ItemType Directory -Force $Build | Out-Null

$Sim = Join-Path $Build "lab04_wave_sim"

$Args = @(
    "-g2005-sv",
    "-I", (Join-Path $Root "rtl\verilog"),
    "-s", "tb_wave_one",
    "-o", $Sim,
    (Join-Path $Root "rtl\verilog\h17_core.v"),
    (Join-Path $Root "labs\support\tb_wave_one.v")
)

Write-Host "== compile LAB-04 waveform test =="
& iverilog @Args
if ($LASTEXITCODE -ne 0) { throw "iverilog failed" }

Write-Host "== run LAB-04 waveform test =="
Push-Location $Root
try {
    & vvp $Sim
    if ($LASTEXITCODE -ne 0) { throw "vvp failed" }
}
finally {
    Pop-Location
}

Write-Host ""
Write-Host "VCD: $Build\h17_lab04.vcd"
Write-Host "Inspect: dut.state, dut.idx, dut.w, dut.k, dut.hits."
