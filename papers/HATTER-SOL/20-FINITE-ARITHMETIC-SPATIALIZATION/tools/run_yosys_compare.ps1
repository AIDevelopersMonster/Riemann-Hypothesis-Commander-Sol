param(
  [int[]]$Widths = @(4,5,6)
)
$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Gen = Join-Path $Lab "generated"
$Out = Join-Path $Lab "yosys_out"
New-Item -ItemType Directory -Force $Out | Out-Null

$yosys = (Get-Command yosys.exe -ErrorAction SilentlyContinue).Source
if (-not $yosys) { $yosys = (Get-Command yosys -ErrorAction SilentlyContinue).Source }
if (-not $yosys) { throw "Yosys not found in PATH" }

py -3 (Join-Path $PSScriptRoot "generate_prime_spatial_lab.py") --out-dir $Gen --widths $Widths
if ($LASTEXITCODE -ne 0) { throw "generator failed" }

$rows = @()

foreach ($w in $Widths) {
  $d = Join-Path $Gen ("w{0}" -f $w)

  foreach ($mode in @("direct","linear","balanced")) {
    $src = (Join-Path $d ("nextprime_{0}.sv" -f $mode)).Replace("\","/")
    $od = Join-Path $Out ("w{0}_{1}" -f $w,$mode)
    New-Item -ItemType Directory -Force $od | Out-Null

    $proc = (Join-Path $od "post_proc.stat").Replace("\","/")
    $tech = (Join-Path $od "post_techmap.stat").Replace("\","/")
    $abc = (Join-Path $od "post_abc.stat").Replace("\","/")
    $json = (Join-Path $od "abc.json").Replace("\","/")

    $cmd = "read_verilog -sv $src; hierarchy -top nextprime_top; proc; flatten; opt; tee -o $proc stat; techmap; opt; tee -o $tech stat; abc -fast; opt; tee -o $abc stat; write_json $json"

    & $yosys -q -p $cmd
    if ($LASTEXITCODE -ne 0) { throw "Yosys failed W=$w mode=$mode" }

    foreach ($stage in @(@("proc",$proc), @("techmap",$tech), @("abc",$abc))) {
      $txt = Get-Content $stage[1] -Raw
      $cells = [regex]::Match($txt, "Number of cells:\s+(\d+)").Groups[1].Value
      $wires = [regex]::Match($txt, "Number of wires:\s+(\d+)").Groups[1].Value
      $bits = [regex]::Match($txt, "Number of wire bits:\s+(\d+)").Groups[1].Value

      $rows += [pscustomobject]@{
        Width = $w
        Mode = $mode
        Stage = $stage[0]
        Cells = [int]$cells
        Wires = [int]$wires
        WireBits = [int]$bits
      }
    }
  }
}

$csv = Join-Path $Lab "PRIME_SPATIAL_YOSYS_SUMMARY.csv"
$rows | Export-Csv -NoTypeInformation -Encoding UTF8 $csv
$rows | Format-Table -AutoSize

Write-Host "CSV: $csv"
