$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H17 = Resolve-Path (Join-Path $Lab "..\..")
$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"

New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

Write-Host "== H17-LAB-03 waveform: generate closure classifiers =="
py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure classifier generator failed" }

Write-Host "== H17-LAB-03 waveform: generate ROM-free repair =="
py -3 (Join-Path $H17 "tools\generate_psl27_romfree_repair.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "ROM-free generator failed" }

$Sim = Join-Path $Build "h17_lab03_wave_sim"
$Sources = @(
    "-g2012",
    "-s", "tb_h17_lab03_waveform",
    "-o", $Sim,
    (Join-Path $Generated "psl27_membership_only.sv"),
    (Join-Path $Generated "psl27_member_class_only.sv"),
    (Join-Path $Generated "psl27_robust8_repair.sv"),
    (Join-Path $Lab "rtl\h17_lab03_sequential_core.sv"),
    (Join-Path $Lab "tb\tb_h17_lab03_waveform.sv")
)

Write-Host "== H17-LAB-03 waveform: compile =="
& iverilog @Sources
if ($LASTEXITCODE -ne 0) { throw "waveform compile failed" }

Write-Host "== H17-LAB-03 waveform: run =="
Push-Location $Lab
try {
    & vvp $Sim
    if ($LASTEXITCODE -ne 0) { throw "waveform simulation failed" }
}
finally {
    Pop-Location
}

$Vcd = Join-Path $Build "h17_lab03_waveform.vcd"
if (!(Test-Path $Vcd)) { throw "VCD not created: $Vcd" }

Write-Host ""
Write-Host "PASS: waveform VCD created:"
Write-Host $Vcd
Write-Host ""
Write-Host "Recommended GTKWave signals:"
Write-Host "  clk rst start busy done"
Write-Host "  dut.state dut.op_idx dut.probe_idx"
Write-Host "  A_in B_in mode_in"
Write-Host "  dut.class_perm dut.class_code"
Write-Host "  raw_signature observed_signature repaired_signature"
Write-Host "  input_valid fingerprint_valid status"
Write-Host ""

$Gtk = Get-Command gtkwave -ErrorAction SilentlyContinue
if ($Gtk) {
    Write-Host "GTKWave found. Opening VCD..."
    & gtkwave $Vcd
} else {
    Write-Host "GTKWave is not in PATH. Open the VCD manually after installing/adding GTKWave."
}
