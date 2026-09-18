# H17-LAB-01 RTL

Этот каталог содержит две эквивалентные HDL-реализации опорного процессора HATTER-SOL-17:

- verilog/ — Verilog-2001;
- vhdl/ — VHDL.

Это reference RTL: понятная последовательная реализация математического контракта H17. Она нужна как эталон для golden-векторов, UART и последующего сравнения с closure-aware / ROM-free ядрами.

## Что вычисляет ядро

Входы A и B — две перестановки по 24 бита, восемь значений по 3 бита:

~~~text
p[3*i +: 3] = p(i), i=0..7
identity = 0xfac688
~~~

Путь данных:

~~~text
A,B
 -> membership in PSL(2,7)
 -> 8 words:
    AAB, Abb, AAAB, Abbb,
    AABAb, AAbAb, ABABB, ABaBB
 -> 8 conjugacy-class codes
 -> raw_signature[23:0]
 -> optional known erasure
 -> observed_signature
 -> compare surviving coordinates with 114 generating-orbit signatures
 -> repaired_signature + legacy orbit_id
~~~

Идея лаборатории: потерять одну из восьми связанных координат и восстановить её по оставшимся семи.

## Файлы

| Файл | Роль |
|---|---|
| verilog/h17_core.v | последовательный reference processor |
| verilog/h17_tables.vh | generated group/orbit/probe tables |
| verilog/h17_uart.v | независимый UART 8N1 |
| verilog/h17_uart_top.v | packet protocol + h17_core |
| vhdl/h17_core.vhd | VHDL-эквивалент ядра |
| vhdl/h17_tables.vhd | package с теми же таблицами |
| vhdl/h17_uart.vhd | VHDL UART |
| vhdl/h17_uart_top.vhd | VHDL packet wrapper |

Таблицы генерируются tools/generate_tables.py. Табличные данные вручную редактировать не следует.

## Class codes и fingerprint

~~~text
0 = 1A
1 = 2A
2 = 3A
3 = 4A
4 = 7A
5 = 7B
7 = erased marker в observed_signature
~~~

Порядок полей:

~~~text
23:21 = AAB
20:18 = Abb
17:15 = AAAB
14:12 = Abbb
11:9  = AABAb
8:6   = AAbAb
5:3   = ABABB
2:0   = ABaBB
~~~

## mode

~~~text
0    без стирания
1    стирается AAB
2    стирается Abb
...
8    стирается ABaBB
>8   ошибка режима
~~~

Номер потерянной координаты известен. В observed_signature соответствующие 3 бита заменяются на 111, а orbit lookup игнорирует их маской.

## status

Точное поведение LAB-01:

~~~text
0 = idle/reset ИЛИ завершённый запрос с A или B вне PSL(2,7)
1 = PSL inputs valid, но generating-orbit match не найден
2 = найден ровно один match
3 = найдено несколько matches
4 = mode > 8
~~~

Поэтому status=0 нельзя трактовать только как «ещё считает». Окончание транзакции определяется done.

orbit_id=127 — invalid/sentinel.

## Почему 1663 такта

Для valid PSL-входа reference FSM выполняет:

~~~text
168      membership scan
1        check
34       letters восьми probe-слов
8 x 168  class scans
1        erasure mask
114      orbit scan
1        finish
----------------
1663 clocks
~~~

Большая задержка намеренная: LAB-01 переиспользует маленький последовательный datapath и является эталоном, а не скоростной архитектурой.

## UART protocol

Request, 12 bytes:

~~~text
A5 5A | 01 | SEQ | MODE | A0 A1 A2 | B0 B1 B2 | CRC8
~~~

Response, 16 bytes:

~~~text
5A A5 | 01 | SEQ | STATUS | ORBIT_ID |
RAW0 RAW1 RAW2 | OBS0 OBS1 OBS2 | REP0 REP1 REP2 | CRC8
~~~

24-битные поля идут little-endian. CRC-8: polynomial 0x07, init 0x00.

Packet status=5 означает bad CRC/version либо mode byte > 15. Mode 9..15 проходит packet layer, но h17_core возвращает status=4.

## LAB-01 и LAB-02

LAB-01:

~~~text
table-driven
sequential
1663 clocks
114-entry orbit lookup
~~~

LAB-02 исследует другой предел:

~~~text
structural membership
closure-aware word/class logic
ROM-free repair
24-bit fingerprint as orbit identity
~~~

LAB-01 не надо оптимизировать до LAB-02: он нужен как независимый reference.

## Границы

Synthesizable RTL сам по себе не означает выбранную FPGA, известную Fmax, LUT/FF/BRAM, timing closure или подтверждённую работу на физической плате.
