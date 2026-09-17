# Digilent Arty A7-35 Rev D/E only. Confirm actual PCB revision before programming.
# Source: https://github.com/Digilent/digilent-xdc/blob/master/Arty-A7-35-Master.xdc
set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports clk100]
create_clock -period 10.000 -name sys_clk [get_ports clk100]
set_property -dict {PACKAGE_PIN D9 IOSTANDARD LVCMOS33} [get_ports btn0]
set_property -dict {PACKAGE_PIN D10 IOSTANDARD LVCMOS33} [get_ports uart_rx]
set_property -dict {PACKAGE_PIN A9 IOSTANDARD LVCMOS33} [get_ports uart_tx]
set_property -dict {PACKAGE_PIN H5 IOSTANDARD LVCMOS33} [get_ports {led[0]}]
set_property -dict {PACKAGE_PIN J5 IOSTANDARD LVCMOS33} [get_ports {led[1]}]
set_property -dict {PACKAGE_PIN T9 IOSTANDARD LVCMOS33} [get_ports {led[2]}]
set_property -dict {PACKAGE_PIN T10 IOSTANDARD LVCMOS33} [get_ports {led[3]}]
# Only asynchronous input-to-FIRST-synchronizer-stage paths are excepted.
# Stage1->stage2 and all computational paths remain timed.
set_false_path -from [get_ports uart_rx] -to [get_pins -hier -filter {NAME =~ */rx_meta_reg/D}]
set_false_path -from [get_ports btn0] -to [get_pins -hier -filter {NAME =~ *bmeta_reg/D}]
# Asynchronous UART output and indicator LEDs have no external synchronous capture clock.
set_false_path -to [get_ports {uart_tx led[*]}]
