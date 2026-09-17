PYTHON ?= python3
IVERILOG ?= iverilog
VVP ?= vvp
GHDL ?= ghdl
VECTORS ?= vectors/quick.txt
VFLAGS ?=
.PHONY: tables test test-verilog test-vhdl uart-verilog uart-vhdl full clean
tables:
	$(PYTHON) tools/generate_tables.py
	$(PYTHON) tools/host.py --generate
test: test-verilog test-vhdl uart-verilog uart-vhdl
test-verilog:
	mkdir -p build
	$(IVERILOG) $(VFLAGS) -g2005-sv -I rtl/verilog -s tb_core -o build/core_sim rtl/verilog/h17_core.v tb/tb_core.v
	$(VVP) build/core_sim +VECTORS=$(VECTORS)
test-vhdl:
	$(GHDL) -a --std=08 rtl/vhdl/h17_tables.vhd rtl/vhdl/h17_core.vhd tb/tb_core.vhd
	$(GHDL) -e --std=08 tb_core
	$(GHDL) -r --std=08 tb_core -gVECTORS=$(VECTORS) --assert-level=error
uart-verilog:
	mkdir -p build
	$(IVERILOG) $(VFLAGS) -g2005-sv -I rtl/verilog -s tb_uart -o build/uart_sim rtl/verilog/*.v tb/tb_uart.v
	$(VVP) build/uart_sim
uart-vhdl:
	$(GHDL) -a --std=08 rtl/vhdl/h17_tables.vhd rtl/vhdl/h17_core.vhd rtl/vhdl/h17_uart.vhd rtl/vhdl/h17_uart_top.vhd tb/tb_uart.vhd
	$(GHDL) -e --std=08 tb_uart
	$(GHDL) -r --std=08 tb_uart --assert-level=error
full:
	$(MAKE) test VECTORS=vectors/full.txt
clean:
	rm -rf build work-obj08.cf
