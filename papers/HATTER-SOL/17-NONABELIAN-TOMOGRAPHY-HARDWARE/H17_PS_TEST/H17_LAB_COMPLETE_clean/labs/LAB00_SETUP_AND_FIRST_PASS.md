# LAB-00 — Развёртывание и первый PASS

## Цель

Получить воспроизводимый H17-LAB-01 на чистом компьютере и отделить ошибки установки от ошибок RTL.

## Задание

1. Установить Git, Python 3, Icarus Verilog.
2. Клонировать репозиторий.
3. Перейти в H17_LAB_COMPLETE_clean.
4. Проверить версии инструментов.
5. Собрать Verilog reference core.
6. Запустить quick vectors.
7. Сохранить PASS и metadata стенда.

## Windows PowerShell

~~~powershell
git --version
py -3 --version
iverilog -V
vvp -V
~~~

Из корня H17_LAB_COMPLETE_clean:

~~~powershell
New-Item -ItemType Directory -Force .\build | Out-Null
iverilog -g2005-sv -I rtl/verilog -s tb_core -o build/core_sim rtl/verilog/h17_core.v tb/tb_core.v
vvp .\build\core_sim +VECTORS=vectors/quick.txt
~~~

Ожидаемая финальная строка:

~~~text
PASS Verilog core: 1796 vectors; valid latency 1663 cycles; busy/reset checked
~~~

## Измерение времени

~~~powershell
Measure-Command {
    vvp .\build\core_sim +VECTORS=vectors/quick.txt
}
~~~

## В отчёт

- ОС и CPU;
- версии инструментов;
- git rev-parse HEAD;
- команда компиляции;
- PASS;
- время выполнения.

## Контрольные вопросы

1. Чем HDL simulation отличается от FPGA synthesis?
2. Что именно означает PASS testbench?
3. Почему PASS не даёт Fmax?
4. Зачем фиксировать commit SHA?
