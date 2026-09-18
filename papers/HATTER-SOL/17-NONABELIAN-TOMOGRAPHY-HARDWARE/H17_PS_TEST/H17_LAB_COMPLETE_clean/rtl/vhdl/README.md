# VHDL RTL

VHDL-ветка реализует тот же H17-LAB-01 contract, что и Verilog.

Файлы:

- h17_tables.vhd — package h17_tables;
- h17_core.vhd — sequential reference core;
- h17_uart.vhd — generic 8N1 UART;
- h17_uart_top.vhd — packet wrapper.

Порядок анализа/компиляции:

~~~text
h17_tables.vhd
h17_core.vhd
h17_uart.vhd
h17_uart_top.vhd
~~~

Golden vectors общие для Verilog и VHDL. Это не отдельная математическая версия H17, а независимое HDL-представление того же reference processor.
