# LAB-04 — FSM, latency и waveform

## Цель

Увидеть математический алгоритм как последовательность цифровых состояний и понять происхождение 1663 тактов.

## FSM LAB-01

~~~text
IDLE
  |
MEMBER
  |
CHECK
  |
WORD <----+
  |       |
CLASSIFY -+
  |
MASK
  |
DECODE
  |
FINISH
  |
IDLE
~~~

## Теоретический расчёт latency

~~~text
168      MEMBER
1        CHECK
34       суммарная длина восьми words
8 x 168  CLASSIFY
1        MASK
114      DECODE
1        FINISH
----------------
1663 clocks
~~~

## Практика

Из корня H17_LAB_COMPLETE_clean:

~~~powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\labs\support\run_lab04_wave.ps1
~~~

Скрипт создаёт:

~~~text
build/h17_lab04.vcd
~~~

Тест использует:

~~~text
A=5e3b88
B=7ecc11
mode=1
~~~

и проверяет:

~~~text
status=2
orbit_id=0
raw=8d256a
observed=ed256a
repaired=8d256a
~~~

## GTKWave

Добавить сигналы:

~~~text
clk
rst
start
busy
done
status
oid
raw
obs
rep
dut.state
dut.idx
dut.w
dut.k
dut.hits
~~~

## Задание

1. Найти start.
2. Найти начало и конец busy.
3. Проверить, что done — импульс.
4. Найти MEMBER -> CHECK -> WORD.
5. Увидеть восемь CLASSIFY scans.
6. Найти MASK и DECODE.
7. Сопоставить waveform с суммой 1663.

## Инженерный вопрос

Почему схема с 1663 тактами может занимать меньше логики, чем комбинационная схема, вычисляющая всё почти за один такт?

Ответ должен обсуждать resource sharing.

## Контрольные вопросы

1. 1663 — математическая нижняя граница?
2. Что такое latency и throughput?
3. Что изменится при нескольких parallel classifier blocks?
4. Почему waveform полезнее одной строки PASS?
