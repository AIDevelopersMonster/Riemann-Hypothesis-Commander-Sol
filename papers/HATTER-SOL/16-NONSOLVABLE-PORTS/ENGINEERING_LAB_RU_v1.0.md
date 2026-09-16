# HATTER-SOL-16 · Контрольная HDL-работа

## Аппаратная демонстрация пятипробового декодера `PSL(2,7)`

**Уровень:** старшие курсы бакалавриата / магистратура / аспирантура.  
**Связь с работой:** приложение к HATTER-SOL-16 v1.1.  
**Публичная демонстрация:** https://www.edaplayground.com/x/Z4Bx

## Цель

Проверить, что доказанная в H16 сигнатура

`A, B, AB, AB^-1, [A,B]`

непосредственно реализуется в синхронном RTL как 15-битный вход, 2-битный канал ориентации `Q4` и 7-битный идентификатор одной из 114 орбит.

## Кодирование

| Класс | Код | Q4 |
|---|---|---|
| `1A` | `000` | `0 / 00` |
| `2A` | `001` | `0 / 00` |
| `3A` | `010` | `0 / 00` |
| `4A` | `011` | `0 / 00` |
| `7A` | `100` | `+1 / 01` |
| `7B` | `101` | `-1 / 10` |

Пять 3-битных кодов упаковываются в

```text
{class_A, class_B, class_AB, class_AB_inv, class_K}
```

и образуют 15-битную сигнатуру. В демонстрационной LUT заданы два golden vector:

```text
011_011_010_011_100 -> orbit 42, Q4=+1
011_011_010_011_101 -> orbit 43, Q4=-1
```

`orbit_id=42/43` здесь являются учебными LUT entries, а не канонической нумерацией полного набора 114 орбит. Полный автоматически сгенерированный ROM относится к H17.

## Локальный CLI

Минимально необходим Icarus Verilog (`iverilog` + `vvp`). GTKWave нужен только для просмотра `dump.vcd`.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install iverilog gtkwave
```

Fedora:

```bash
sudo dnf install iverilog gtkwave
```

macOS + Homebrew:

```bash
brew install icarus-verilog gtkwave
```

Windows 10/11: рекомендуемый воспроизводимый путь — WSL2 (`wsl --install`), затем Ubuntu-команды выше. Native-вариант через MSYS2 UCRT64:

```bash
pacman -S mingw-w64-ucrt-x86_64-iverilog mingw-w64-ucrt-x86_64-gtkwave
```

При вызове из `cmd.exe` добавьте `C:\msys64\ucrt64\bin` в `PATH`.

Проверка:

```bash
iverilog -V
vvp -V
gtkwave --version
```

Сборка и запуск:

```bash
iverilog -g2012 -Wall -s tb_h16_orbit_decoder -o h16_sim h16_orbit_decoder.v tb_h16_orbit_decoder.v
vvp h16_sim
```

Осциллограмма:

```bash
gtkwave dump.vcd
```

В Zenodo-пакете также находятся `Makefile`, `run_h16_cli.sh`, `run_h16_cli.bat`, интерактивный HTML-demo и снимок EPWave.

## Практическая значимость

Контрольная работа соединяет математический результат H16 с реальным цифровым трактом. После классового распознавания достаточно 15 входных бит, двух orientation bits и 7-битного orbit ID. Студент проходит весь маршрут `теорема -> кодирование -> RTL -> testbench -> waveform`; аспирант может продолжить его автоматической генерацией полного 114-entry ROM, исследованием fault/erasure robustness, синтезом и FPGA-валидацией.

## Рекомендуемые задания

1. Добавить assertion для запрещённых class codes `110` и `111`.
2. Проверить latency `valid_in -> valid_out`.
3. Добавить negative vector и проверить `7'h7F`.
4. Сгенерировать ROM из CSV вместо ручного `case`.
5. Сравнить case/LUT/BRAM реализации по ресурсу и задержке.
6. Подготовить H17-версию с полным набором 114 сигнатур и exhaustive RTL test.

H16 не утверждает timing closure, fixed-point noise margin, устойчивость к ошибкам или физическую реализацию на плате; это программа H17.