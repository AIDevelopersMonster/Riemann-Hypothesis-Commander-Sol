package require ::quartus::project
package require ::quartus::sta

project_open h18_r12_comb_115k_c7
create_timing_netlist
read_sdc
set_operating_conditions -model slow -temperature 85 -voltage 1200
update_timing_netlist
report_timing -setup -from_clock clk -to_clock clk -npaths 3 -detail full_path -show_routing -file worst_path_full.rpt
delete_timing_netlist
project_close
