transcript on
onerror {quit -code 1}
add wave -divider {POST-FIT TRANSACTION}
add wave sim:/tb_h17_lab02_postfit/clk
add wave sim:/tb_h17_lab02_postfit/rst
add wave sim:/tb_h17_lab02_postfit/start
add wave -radix hex sim:/tb_h17_lab02_postfit/a_in
add wave -radix hex sim:/tb_h17_lab02_postfit/b_in
add wave -radix unsigned sim:/tb_h17_lab02_postfit/mode_in
add wave sim:/tb_h17_lab02_postfit/busy
add wave sim:/tb_h17_lab02_postfit/done
add wave -divider {POST-FIT RESULT}
add wave -radix unsigned sim:/tb_h17_lab02_postfit/status
add wave sim:/tb_h17_lab02_postfit/input_valid
add wave sim:/tb_h17_lab02_postfit/fingerprint_valid
add wave -radix hex sim:/tb_h17_lab02_postfit/raw_signature
add wave -radix hex sim:/tb_h17_lab02_postfit/observed_signature
add wave -radix hex sim:/tb_h17_lab02_postfit/repaired_signature
log sim:/tb_h17_lab02_postfit/*
run -all
wave zoom full
