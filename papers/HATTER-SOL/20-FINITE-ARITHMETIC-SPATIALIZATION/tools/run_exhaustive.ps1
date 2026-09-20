param(
  [int[]]$Widths = @(4,5,6)
)
$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Gen = Join-Path $Lab "generated"

$iverilog = (Get-Command iverilog.exe -ErrorAction SilentlyContinue).Source
if (-not $iverilog) { $iverilog = (Get-Command iverilog -ErrorAction SilentlyContinue).Source }
if (-not $iverilog -and (Test-Path "C:\iverilog\bin\iverilog.exe")) { $iverilog = "C:\iverilog\bin\iverilog.exe" }

$vvp = (Get-Command vvp.exe -ErrorAction SilentlyContinue).Source
if (-not $vvp) { $vvp = (Get-Command vvp -ErrorAction SilentlyContinue).Source }
if (-not $vvp -and (Test-Path "C:\iverilog\bin\vvp.exe")) { $vvp = "C:\iverilog\bin\vvp.exe" }

if (-not $iverilog -or -not $vvp) {
  throw "Icarus Verilog not found (iverilog/vvp)"
}

py -3 (Join-Path $PSScriptRoot "generate_prime_spatial_lab.py") --out-dir $Gen --widths $Widths
if ($LASTEXITCODE -ne 0) { throw "generator failed" }

foreach ($w in $Widths) {
  $d = Join-Path $Gen ("w{0}" -f $w)

  Write-Host "== W=$w prime membership =="
  & $iverilog -g2012 -s tb -o (Join-Path $d "sim_member.vvp") (Join-Path $d "prime_member_direct.sv") (Join-Path $d "tb_prime_member.sv")
  if ($LASTEXITCODE -ne 0) { throw "iverilog membership W=$w failed" }

  & $vvp (Join-Path $d "sim_member.vvp")
  if ($LASTEXITCODE -ne 0) { throw "vvp membership W=$w failed" }

  foreach ($mode in @("direct","linear","balanced")) {
    Write-Host "== W=$w nextPrime $mode =="

    $src = Join-Path $d ("nextprime_{0}.sv" -f $mode)
    $sim = Join-Path $d ("sim_{0}.vvp" -f $mode)

    & $iverilog -g2012 -s tb -o $sim $src (Join-Path $d "tb_nextprime.sv")
    if ($LASTEXITCODE -ne 0) { throw "iverilog W=$w mode=$mode failed" }

    & $vvp $sim
    if ($LASTEXITCODE -ne 0) { throw "vvp W=$w mode=$mode failed" }
  }
}

Write-Host "PASS: all finite prime representations are exhaustively equivalent"
