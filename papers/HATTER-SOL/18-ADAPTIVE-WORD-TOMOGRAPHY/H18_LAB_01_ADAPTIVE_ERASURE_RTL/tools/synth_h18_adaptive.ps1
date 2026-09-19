$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H18 = Resolve-Path (Join-Path $Lab "..")
$H17 = Resolve-Path (Join-Path $H18 "..\17-NONABELIAN-TOMOGRAPHY-HARDWARE")
$Generated = Join-Path $Lab "generated"
$Build = Join-Path $Lab "build"
New-Item -ItemType Directory -Force $Generated | Out-Null
New-Item -ItemType Directory -Force $Build | Out-Null

py -3 (Join-Path $Lab "tools\generate_h18_adaptive_controller.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "adaptive generator failed" }

py -3 (Join-Path $H17 "tools\generate_psl27_closure_classifiers.py") --out-dir $Generated
if ($LASTEXITCODE -ne 0) { throw "closure classifier generator failed" }

$Yosys = Get-Command yosys -ErrorAction SilentlyContinue
if (-not $Yosys) {
    throw "yosys not found in PATH"
}

$Script = @"
read_verilog -sv "$Generated/psl27_membership_only.sv"
read_verilog -sv "$Generated/psl27_member_class_only.sv"
read_verilog -sv "$Generated/h18_adaptive_word_rom.sv"
read_verilog -sv "$Generated/h18_adaptive_controller_rom.sv"
read_verilog -sv "$Lab/rtl/h18_adaptive_sequential_core.sv"
hierarchy -check -top h18_adaptive_sequential_core
proc
opt
fsm
opt
memory
opt
techmap
opt
abc -g AND,OR,XOR,XNOR,MUX
clean
stat
"@

$Ys = Join-Path $Build "h18_adaptive_generic.ys"
$Log = Join-Path $Build "h18_adaptive_generic_yosys.log"
Set-Content -Path $Ys -Value $Script -Encoding ascii

& $Yosys.Source -s $Ys 2>&1 | Tee-Object -FilePath $Log
if ($LASTEXITCODE -ne 0) { throw "yosys synthesis failed" }

Write-Host ""
Write-Host "Saved generic synthesis log:"
Write-Host $Log
Write-Host ""
Write-Host "Compare this under the SAME Yosys version/methodology with H17-LAB-03."
