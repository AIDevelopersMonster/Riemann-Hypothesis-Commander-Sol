transcript on
log -r /*
add wave sim:/tb_h17_lab02_waveform/clk
add wave sim:/tb_h17_lab02_waveform/rst
add wave sim:/tb_h17_lab02_waveform/start
add wave -radix hex sim:/tb_h17_lab02_waveform/a_in
add wave -radix hex sim:/tb_h17_lab02_waveform/b_in
add wave -radix unsigned sim:/tb_h17_lab02_waveform/mode_in
add wave sim:/tb_h17_lab02_waveform/busy
add wave sim:/tb_h17_lab02_waveform/done
add wave -radix unsigned sim:/tb_h17_lab02_waveform/status
add wave sim:/tb_h17_lab02_waveform/input_valid
add wave sim:/tb_h17_lab02_waveform/fingerprint_valid
add wave -radix hex sim:/tb_h17_lab02_waveform/raw_signature
add wave -radix hex sim:/tb_h17_lab02_waveform/observed_signature
add wave -radix hex sim:/tb_h17_lab02_waveform/repaired_signature
add wave -divider LATCED_INPUTS
add wave -radix hex sim:/tb_h17_lab02_waveform/dut/a_q
add wave -radix hex sim:/tb_h17_lab02_waveform/dut/b_q
add wave -radix unsigned sim:/tb_h17_lab02_waveform/dut/mode_q
add wave sim:/tb_h17_lab02_waveform/dut/pending
add wave -divider CORE
add wave -radix hex sim:/tb_h17_lab02_waveform/dut/u_core/engine_signature
add wave sim:/tb_h17_lab02_waveform/dut/u_core/raw_membership_valid
add wave sim:/tb_h17_lab02_waveform/dut/u_core/repair_valid
add wave -radix hex sim:/tb_h17_lab02_waveform/dut/u_core/repair_signature
run -all
wave zoom full
