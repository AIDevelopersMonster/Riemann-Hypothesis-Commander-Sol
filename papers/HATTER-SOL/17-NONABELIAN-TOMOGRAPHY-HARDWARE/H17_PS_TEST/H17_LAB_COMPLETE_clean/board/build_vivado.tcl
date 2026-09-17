# Run from package root: vivado -mode batch -source board/build_vivado.tcl -tclargs verilog
set lang [lindex $argv 0]
if {$lang ni {verilog vhdl}} {error "choose verilog or vhdl"}
set out build_$lang
file mkdir $out
create_project h17_$lang $out -part xc7a35ticsg324-1L -force
if {$lang eq "verilog"} {
 set_property include_dirs [list [file normalize rtl/verilog]] [current_fileset]
 read_verilog [glob rtl/verilog/*.v]
 read_verilog board/h17_arty.v
} else {
 read_vhdl -vhdl2008 rtl/vhdl/h17_tables.vhd
 read_vhdl -vhdl2008 rtl/vhdl/h17_core.vhd
 read_vhdl -vhdl2008 rtl/vhdl/h17_uart.vhd
 read_vhdl -vhdl2008 rtl/vhdl/h17_uart_top.vhd
 read_vhdl -vhdl2008 board/h17_arty.vhd
}
read_xdc board/arty_a7_35.xdc
synth_design -top h17_arty -part xc7a35ticsg324-1L
report_utilization -hierarchical -file $out/utilization_synth.rpt
opt_design
place_design
phys_opt_design
route_design
report_utilization -file $out/utilization_route.rpt
report_timing_summary -delay_type min_max -report_unconstrained -file $out/timing.rpt
report_clock_interaction -file $out/clocks.rpt
report_cdc -file $out/cdc.rpt
report_drc -file $out/drc.rpt
check_timing -verbose -file $out/check_timing.rpt
write_checkpoint -force $out/routed.dcp
set worst_setup [get_timing_paths -delay_type max -max_paths 1]
set worst_hold [get_timing_paths -delay_type min -max_paths 1]
if {[llength $worst_setup]==0 || [llength $worst_hold]==0} {error "No timing paths; inspect constraints"}
if {[get_property SLACK $worst_setup]<0 || [get_property SLACK $worst_hold]<0} {error "Timing failed; bitstream deliberately not generated"}
# Inspect CDC/check_timing/DRC before use; this is not a blanket timing waiver.
write_bitstream -force $out/h17_arty.bit
