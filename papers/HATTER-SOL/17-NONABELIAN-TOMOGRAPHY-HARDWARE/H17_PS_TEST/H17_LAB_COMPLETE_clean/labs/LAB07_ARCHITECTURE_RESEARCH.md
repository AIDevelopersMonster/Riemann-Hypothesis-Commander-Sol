# LAB-07 — Исследовательская работа: площадь против latency

## Цель

Перейти от вопроса «код работает?» к вопросу «какую архитектуру выбрать при той же математической функции?».

## LAB-01

~~~text
один последовательный datapath
многократные table scans
1663 clocks
~~~

Плюсы: читаемость, простая верификация, сильное resource sharing.

Минусы: большая latency, orbit table в backend.

## Structural H17

В H17-07/H17-08 используется другой подход:

~~~text
shared word DAG
structural membership
class-only derived words
ROM-free repair
~~~

Полностью развёрнутая версия уменьшает latency, но создаёт большую комбинационную сеть.

## Исследовательское задание

Спроектировать промежуточную архитектуру, например:

~~~text
2 membership checks
1 shared permutation composition unit
1 shared class engine
8 x 3-bit fingerprint registers
ROM-free repair
controller FSM
~~~

Оценить:

1. число функциональных блоков;
2. число тактов на transaction;
3. где нужны registers;
4. где возможен pipeline;
5. какие таблицы остаются;
6. какие таблицы исчезают;
7. отличие от LAB-01 и fully-unrolled core.

## Обязательная block diagram

~~~text
INPUT LATCH
    |
MEMBERSHIP
    |
WORD ENGINE
    |
CLASS ENGINE
    |
FINGERPRINT REGS
    |
REPAIR
    |
OUTPUT
~~~

## Advanced theory

Использовать closure:

~~~text
A,B in PSL(2,7)  =>  w(A,B) in PSL(2,7)
~~~

Объяснить, почему после membership исходных A,B не надо повторять полный membership test для каждого derived word.

## Что нельзя утверждать без измерения

До target-specific synthesis/place-and-route нельзя выдавать предположение за факт:

~~~text
эта FPGA точно подходит
Fmax = ...
power = ...
ровно N LUT
~~~

## Итог

Защитить trade-off:

~~~text
area <-> latency <-> throughput
~~~
