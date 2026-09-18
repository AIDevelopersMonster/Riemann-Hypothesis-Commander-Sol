# Verilog RTL

Файлы:

- h17_core.v — sequential H17-LAB-01 reference core;
- h17_tables.vh — generated data included by h17_core.v;
- h17_uart.v — generic 8N1 UART;
- h17_uart_top.v — 12-byte request / 16-byte response wrapper.

Для понимания архитектуры сначала читайте ../README.md и header/FSM в h17_core.v. h17_tables.vh — generated data, а не скрытый алгоритм.

Quick reference test из корня H17_LAB_COMPLETE_clean:

~~~powershell
New-Item -ItemType Directory -Force .\build | Out-Null
iverilog -g2005-sv -I rtl/verilog -s tb_core -o build/core_sim rtl/verilog/h17_core.v tb/tb_core.v
vvp .\build\core_sim +VECTORS=vectors/quick.txt
~~~

Ожидаемый результат:

~~~text
PASS Verilog core: 1796 vectors; valid latency 1663 cycles; busy/reset checked
~~~
