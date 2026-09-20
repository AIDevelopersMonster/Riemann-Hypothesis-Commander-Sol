param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("direct","balanced","linear")]
  [string]$Mode,

  [Parameter(Mandatory=$true)]
  [ValidateSet(8,9,10)]
  [int]$Width
)

$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$H20 = (Resolve-Path (Join-Path $Lab "..")).Path

$GenRoot = Join-Path $Lab "generated"
$WDir = Join-Path $GenRoot ("w{0}" -f $Width)
$QDir = Join-Path $Lab ("quartus13_cyclonev_a7\w{0}_{1}" -f $Width,$Mode)
$Project = "h20_w{0}_{1}_cv_a7" -f $Width,$Mode

New-Item -ItemType Directory -Force $GenRoot | Out-Null
New-Item -ItemType Directory -Force $QDir | Out-Null

Write-Host "== H20-LAB-01 PRIME Cyclone V =="
Write-Host ("Width: W={0}" -f $Width)
Write-Host ("Mode: {0}" -f $Mode)
Write-Host "Target: 5CEFA7F23C6"
Write-Host "Clock contract: 100 MHz"

py -3 (Join-Path $H20 "tools\generate_prime_spatial_lab.py") --out-dir $GenRoot --widths $Width
if ($LASTEXITCODE -ne 0) { throw "prime RTL generation failed" }

$Source = Join-Path $WDir ("nextprime_{0}.sv" -f $Mode)
if (!(Test-Path $Source)) { throw "generated source missing: $Source" }

$Wrapper = Join-Path $QDir "nextprime_registered_top.sv"
$OW = $Width + 1
$WrapperText = @"
module nextprime_registered_top(
  input  logic clk,
  input  logic [$($Width-1):0] x,
  output logic [$($OW-1):0] p
);
  logic [$($Width-1):0] x_q;
  logic [$($OW-1):0] p_comb;

  always_ff @(posedge clk) begin
    x_q <= x;
    p   <= p_comb;
  end

  nextprime_top u_core(
    .x(x_q),
    .p(p_comb)
  );
endmodule
"@
Set-Content -Path $Wrapper -Value $WrapperText -Encoding ascii

function QPath([string]$p) {
  return ([System.IO.Path]::GetFullPath($p) -replace '\\','/')
}

$SourceQ = QPath $Source
$WrapperQ = QPath $Wrapper

$Qsf = @"
set_global_assignment -name FAMILY "Cyclone V"
set_global_assignment -name DEVICE 5CEFA7F23C6
set_global_assignment -name TOP_LEVEL_ENTITY nextprime_registered_top
set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files
set_global_assignment -name SYSTEMVERILOG_FILE "$SourceQ"
set_global_assignment -name SYSTEMVERILOG_FILE "$WrapperQ"
set_global_assignment -name SDC_FILE $Project.sdc
set_global_assignment -name RESERVE_ALL_UNUSED_PINS "AS INPUT TRI-STATED"
"@
Set-Content -Path (Join-Path $QDir "$Project.qsf") -Value $Qsf -Encoding ascii
Set-Content -Path (Join-Path $QDir "$Project.sdc") -Value 'create_clock -name clk -period 10.000 [get_ports {clk}]' -Encoding ascii

$Tcl = @"
package require ::quartus::project
package require ::quartus::sta

project_open $Project
create_timing_netlist
read_sdc
set_operating_conditions -model slow -temperature 85 -voltage 1100
update_timing_netlist
report_timing -setup -from_clock clk -to_clock clk -npaths 3 -detail full_path -show_routing -file worst_path_full.rpt
delete_timing_netlist
project_close
"@
Set-Content -Path (Join-Path $QDir "worst_path.tcl") -Value $Tcl -Encoding ascii

$QuartusExe = "C:\altera\13.1\quartus\bin64\quartus_sh.exe"
$StaExe = "C:\altera\13.1\quartus\bin64\quartus_sta.exe"

if (!(Test-Path $QuartusExe)) { throw "Quartus II 13.1 not found at $QuartusExe" }
if (!(Test-Path $StaExe)) { throw "quartus_sta.exe not found at $StaExe" }

Push-Location $QDir
try {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  & $QuartusExe --flow compile $Project
  $rc = $LASTEXITCODE
  $sw.Stop()

  Write-Host ("H20 W={0} {1} CYCLONE V COMPILE ELAPSED: {2:N3} seconds" -f $Width,$Mode,$sw.Elapsed.TotalSeconds)

  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  $Map = Join-Path $QDir "output_files\$Project.map.rpt"
  $Sta = Join-Path $QDir "output_files\$Project.sta.rpt"

  Write-Host "== UTILIZATION =="
  foreach ($rpt in @($Fit,$Map)) {
    if (Test-Path $rpt) {
      Select-String -Path $rpt -Pattern "Logic utilization","Total ALMs","Total combinational ALUTs","Dedicated logic registers","Total registers","Total memory bits","Total pins","DSP" |
        Select-Object -First 180 | ForEach-Object { $_.Line }
    }
  }

  Write-Host "== TIMEQUEST =="
  if (Test-Path $Sta) {
    Select-String -Path $Sta -Pattern "Fmax Summary","Restricted Fmax","Worst-case setup slack","Worst-case hold slack","Setup Summary","Hold Summary","MHz" -Context 0,8 |
      Select-Object -First 240
  }

  if ($rc -ne 0) {
    Write-Host "NO ROUTED WORST PATH: Quartus compile did not complete successfully."
    exit $rc
  }

  Write-Host "== DETAILED WORST PATH =="
  & $StaExe -t .\worst_path.tcl
  if ($LASTEXITCODE -ne 0) { throw "worst-path report failed" }

  Get-Content .\worst_path_full.rpt

  Write-Host ("PASS H20-LAB-01 W={0} {1} on 5CEFA7F23C6" -f $Width,$Mode)
}
finally {
  Pop-Location
}
