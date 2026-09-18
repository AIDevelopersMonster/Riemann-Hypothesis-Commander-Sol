# LAB-06 — Один процессор на Verilog и VHDL

## Цель

Показать, что H17 contract не зависит от одного HDL-языка.

## Реализации

~~~text
rtl/verilog/
rtl/vhdl/
~~~

Обе используют общие golden vectors.

## Verilog

~~~powershell
iverilog -g2005-sv -I rtl/verilog -s tb_core -o build/core_sim rtl/verilog/h17_core.v tb/tb_core.v
vvp .\build\core_sim +VECTORS=vectors/quick.txt
~~~

## VHDL

Нужен GHDL:

~~~powershell
ghdl --version
ghdl -a --std=08 rtl/vhdl/h17_tables.vhd rtl/vhdl/h17_core.vhd tb/tb_core.vhd
ghdl -e --std=08 tb_core
ghdl -r --std=08 tb_core -gVECTORS=vectors/quick.txt --assert-level=error
~~~

## Задание

1. Получить PASS Verilog.
2. Получить PASS VHDL.
3. Сравнить compose, inverse, FSM, MASK и DECODE.
4. Найти минимум три места, где языки по-разному выражают одну операцию.

## Продвинутый вопрос

Два независимых HDL PASS повышают доверие, но являются ли формальным доказательством эквивалентности реализаций для всех состояний? Обоснуйте.

## Отчёт

Приложить обе финальные строки PASS и версии Icarus/GHDL.
