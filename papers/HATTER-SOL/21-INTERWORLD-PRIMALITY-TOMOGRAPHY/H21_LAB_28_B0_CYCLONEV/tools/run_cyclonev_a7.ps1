param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("scalar","quadratic")]
  [string]$Mode
)

$ErrorActionPreference = "Stop"

$Lab = Resolve-Path (Join-Path $PSScriptRoot "..")
$H21 = Resolve-Path (Join-Path $Lab "..")
$Lab27 = Join-Path $H21 "H21_LAB_27_B0_RTL"

$QDir = Join-Path $Lab ("quartus13_cyclonev_a7\" + $Mode)
$Project = "h21_b0_" + $Mode + "_cv_a7"
$Top = if ($Mode -eq "scalar") { "h21_scalar_pow" } else { "h21_quad_pow_b0" }

New-Item -ItemType Directory -Force $QDir | Out-Null

Write-Host "== H21-LAB-28 B=0 Cyclone V =="
Write-Host ("Mode: {0}" -f $Mode)
Write-Host ("Top: {0}" -f $Top)
Write-Host "Target: 5CEFA7F23C6"

$Qsf = @"
set_global_assignment -name FAMILY "Cyclone V"
set_global_assignment -name DEVICE 5CEFA7F23C6
set_global_assignment -name TOP_LEVEL_ENTITY $Top
set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files
set_global_assignment -name SYSTEMVERILOG_FILE ../../../H21_LAB_27_B0_RTL/h21_b0_cores.sv
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

  Write-Host ("H21 {0} CYCLONE V COMPILE ELAPSED: {1:N3} seconds" -f $Mode,$sw.Elapsed.TotalSeconds)

  $Fit = Join-Path $QDir "output_files\$Project.fit.rpt"
  $Map = Join-Path $QDir "output_files\$Project.map.rpt"
  $Sta = Join-Path $QDir "output_files\$Project.sta.rpt"

  Write-Host "== UTILIZATION =="
  foreach ($rpt in @($Fit,$Map)) {
    if (Test-Path $rpt) {
      Select-String -Path $rpt -Pattern "Logic utilization","Total ALMs","ALMs","Total combinational ALUTs","Dedicated logic registers","Total registers","Total memory bits","Total pins","DSP" |
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

  & $StaExe -t .\worst_path.tcl
  if ($LASTEXITCODE -ne 0) { throw "worst-path report failed" }

  Write-Host "PASS H21-LAB-28 $Mode on 5CEFA7F23C6"
}
finally {
  Pop-Location
}
