# LAB-05 — UART, CRC и ошибки протокола

## Цель

Отделить математическое ядро от транспортного слоя и проверить, что ошибки UART-пакета не превращаются в математические результаты.

## Архитектура

~~~text
PC / host.py
    |
 USB-UART
    |
h17_uart
    |
h17_uart_top
    |
h17_core
~~~

## Request

12 bytes:

~~~text
A5 5A | VERSION | SEQ | MODE | A(3 bytes LE) | B(3 bytes LE) | CRC8
~~~

## Response

16 bytes:

~~~text
5A A5 | VERSION | SEQ | STATUS | ORBIT_ID |
RAW(3) | OBSERVED(3) | REPAIRED(3) | CRC8
~~~

CRC polynomial: 0x07.

## Подготовка UART vectors

~~~powershell
py -3 .\tools\host.py --generate
~~~

## Компиляция

~~~powershell
New-Item -ItemType Directory -Force .\build | Out-Null
iverilog -g2005-sv -I rtl/verilog -s tb_uart -o build/uart_sim rtl/verilog/h17_core.v rtl/verilog/h17_uart.v rtl/verilog/h17_uart_top.v tb/tb_uart.v
vvp .\build\uart_sim
~~~

Testbench проверяет:

- bad CRC;
- bad version;
- wide mode byte;
- framing error;
- truncated frame timeout;
- parser recovery после плохого запроса.

## Задание

1. Нарисовать request frame.
2. Нарисовать response frame.
3. Найти CRC function.
4. Найти timeout parser.
5. Объяснить разницу между packet status=5 и core status=4.
6. Найти хороший и ошибочный transaction в vectors/uart.txt.

## Углубление

Почему CRC защищает транспорт, но не доказывает правильность математического алгоритма?

## Контрольные вопросы

1. Зачем magic bytes A5 5A?
2. Зачем sequence number?
3. Почему A и B little-endian?
4. Что должен делать parser после оборванного кадра?
