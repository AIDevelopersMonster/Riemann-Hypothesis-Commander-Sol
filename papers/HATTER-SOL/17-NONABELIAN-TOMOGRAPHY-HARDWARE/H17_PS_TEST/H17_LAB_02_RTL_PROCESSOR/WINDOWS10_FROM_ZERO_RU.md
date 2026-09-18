# H17-LAB-02 · Windows 10 from zero

Эта инструкция предназначена для проверки H17-LAB-02 на чистом компьютере с
Windows 10. Для лаборатории не требуется FPGA, Vivado, Quartus, Gowin IDE,
WSL или Linux.

Нужны только:

- Git;
- Python 3;
- Icarus Verilog (`iverilog` + `vvp`);
- PowerShell, который уже входит в Windows 10.

Цель проверки:

```text
чистая Windows 10
 -> получить исходники из GitHub
 -> проверить инструменты
 -> сгенерировать closure-aware RTL
 -> сгенерировать ROM-free repair RTL
 -> скомпилировать H17-LAB-02
 -> один smoke vector
 -> quick = 1 796 vectors
 -> full = 29 911 vectors
```

---

## 0. Открыть PowerShell

Все команды ниже выполняются в обычном PowerShell.

Права администратора для самой лаборатории не нужны.

Проверить версию Windows:

```powershell
winver
```

Проверить наличие Windows Package Manager:

```powershell
winget --version
```

Если команда `winget` существует, переходите к следующему шагу.

Если `winget` отсутствует, установите/обновите Microsoft App Installer, затем
откройте новое окно PowerShell. Сам H17 от `winget` не зависит; это только
удобный способ поставить три инструмента.

---

## 1. Установить Git

```powershell
winget install --id Git.Git -e
```

После установки закройте PowerShell и откройте его снова.

Проверка:

```powershell
git --version
```

Должна появиться строка с версией Git.

---

## 2. Установить Python 3

```powershell
winget install --id Python.Python.3.12 -e
```

Закройте PowerShell и откройте снова.

Проверка:

```powershell
py -3 --version
```

Дополнительная проверка:

```powershell
py -3 -c "print('PYTHON OK')"
```

Ожидается:

```text
PYTHON OK
```

Внешние Python-пакеты H17-LAB-02 не требуются.

---

## 3. Установить Icarus Verilog

```powershell
winget install --id Icarus.Verilog -e
```

Снова откройте новое окно PowerShell.

Проверка:

```powershell
iverilog -V
vvp -V
```

Если Windows установила Icarus в `C:\iverilog`, но команды пока не находятся,
для текущего окна выполните:

```powershell
$env:Path += ";C:\iverilog\bin"
```

и повторите:

```powershell
iverilog -V
vvp -V
```

Для постоянного добавления в пользовательский PATH:

```powershell
$old = [Environment]::GetEnvironmentVariable("Path","User")
if ($old -notlike "*C:\iverilog\bin*") {
    [Environment]::SetEnvironmentVariable("Path", $old + ";C:\iverilog\bin", "User")
}
```

После этого откройте новое окно PowerShell.

GTKWave для первых тестов не нужен.

---

## 4. Получить репозиторий

Создаём обычную рабочую папку в Documents:

```powershell
New-Item -ItemType Directory -Force "$HOME\Documents\GitHub" | Out-Null
cd "$HOME\Documents\GitHub"
```

Клонируем:

```powershell
git clone https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol.git
cd .\Riemann-Hypothesis-Commander-Sol
```

Получаем ветку LAB-02:

```powershell
git fetch origin
git switch --track origin/research/hatter-sol-17-lab02-romfree-rtl
```

Проверяем:

```powershell
git branch --show-current
```

Ожидается:

```text
research/hatter-sol-17-lab02-romfree-rtl
```

---

## 5. Перейти в лабораторию

```powershell
cd .\papers\HATTER-SOL\17-NONABELIAN-TOMOGRAPHY-HARDWARE\H17_PS_TEST\H17_LAB_02_RTL_PROCESSOR
```

Проверить содержимое:

```powershell
Get-ChildItem
```

Должны присутствовать как минимум:

```text
rtl
tb
tools
README_RU.md
STATUS.md
WINDOWS10_FROM_ZERO_RU.md
```

---

## 6. Разрешить локальные PS1 только для этого окна

На части Windows 10 выполнение сценариев PowerShell выключено.

Без изменения системной политики:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Если PowerShell просит подтверждение, ответьте `Y`.

Эта настройка исчезнет после закрытия данного окна.

Альтернатива: любой скрипт можно запускать отдельной командой вида

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tools\check_environment.ps1
```

---

## 7. Проверить окружение H17

```powershell
.\tools\check_environment.ps1
```

В конце должно быть:

```text
PASS H17 Windows environment
```

Если здесь ошибка, RTL ещё не запускаем: сначала исправляем окружение.

---

## 8. Первый контроль: LAB-01 reference core

Этот шаг не обязателен математически, но очень полезен на новом компьютере:
он отделяет проблему установки Icarus от проблемы новой архитектуры LAB-02.

Перейти в LAB-01:

```powershell
cd ..\H17_LAB_COMPLETE_clean
```

Создать build и скомпилировать reference core:

```powershell
New-Item -ItemType Directory -Force .\build | Out-Null

iverilog `
  -g2005-sv `
  -I rtl/verilog `
  -s tb_core `
  -o build/core_sim `
  rtl/verilog/h17_core.v `
  tb/tb_core.v
```

Запустить quick:

```powershell
vvp .\build\core_sim +VECTORS=vectors/quick.txt
```

Ожидается:

```text
PASS Verilog core: 1796 vectors; valid latency 1663 cycles; busy/reset checked
```

Вернуться в LAB-02:

```powershell
cd ..\H17_LAB_02_RTL_PROCESSOR
```

---

## 9. LAB-02: один smoke vector

Сначала не запускаем 1 796 случаев. Проверяем ровно один уже известный
генерирующий пример:

```powershell
.\tools\test_smoke.ps1
```

Скрипт:

1. запускает H17-08 generator;
2. запускает H17-06 ROM-free generator;
3. компилирует чистый LAB-02;
4. создаёт один vector;
5. запускает `vvp`;
6. измеряет время.

Тестовый пример:

```text
A        = 5e3b88
B        = 7ecc11
mode     = 1
status   = 2
raw      = 8d256a
observed = ed256a
repaired = 8d256a
```

Нормальный функциональный итог:

```text
PASS H17-LAB-02 pure RTL: 1 vectors; closure-aware frontend + ROM-free fingerprint
```

Если один vector не завершился за разумное время, фиксируем фактическое время
и не запускаем quick/full вслепую.

---

## 10. LAB-02 quick

После smoke:

```powershell
.\tools\test_lab02.ps1 -Set quick
```

Набор содержит 1 796 строк.

Testbench периодически выводит:

```text
PROGRESS H17-LAB-02: ...
```

Это позволяет отличить медленную симуляцию от остановившегося процесса.

Финальный ожидаемый результат:

```text
PASS H17-LAB-02 pure RTL: 1796 vectors; closure-aware frontend + ROM-free fingerprint
```

### Важное замечание о скорости

LAB-02 сейчас является почти полностью развёрнутой комбинационной архитектурой.
Icarus — event-driven simulator. Поэтому программная симуляция может быть
намного медленнее LAB-01 даже при том, что аппаратная архитектура потенциально
имеет намного меньшую латентность.

Длительное время `vvp` не является измерением будущей скорости FPGA.

---

## 11. Как проверить жив ли vvp

В другом окне PowerShell:

```powershell
Get-Process vvp | Select-Object Id,CPU,StartTime,WorkingSet64
```

Повторите через минуту.

Рост поля `CPU` означает, что процесс исполняется, но главный индикатор после
этой версии testbench — строки `PROGRESS`.

Если нажать `Ctrl+C`, `vvp` может перейти в интерактивный prompt:

```text
>
```

Продолжить:

```text
cont
```

Завершить:

```text
finish
```

---

## 12. LAB-02 controller quick

После успешного pure-core quick:

```powershell
.\tools\test_controller.ps1 -Set quick
```

Он дополнительно проверяет:

- защёлкивание входов по `start`;
- игнорирование изменения внешних A/B во время `busy`;
- однотактный `done`;
- reset незавершённой операции.

Ожидаемый итог:

```text
PASS H17-LAB-02 controller: 1796 vectors; input latch, busy/done and reset checked
```

---

## 13. Full regression

Только после успешных smoke и quick:

```powershell
.\tools\test_lab02.ps1 -Set full
```

и затем:

```powershell
.\tools\test_controller.ps1 -Set full
```

Full содержит 29 911 golden vectors.

На текущей полностью комбинационной архитектуре этот тест может быть очень
долгим. Это исследовательский exhaustive regression, а не повседневный smoke.

---

## 14. Что прислать для воспроизводимости

С нового компьютера сохранить вывод:

```powershell
git rev-parse HEAD
git branch --show-current
git status --short
git --version
py -3 --version
iverilog -V
vvp -V
```

И результаты:

```text
LAB-01 quick
LAB-02 smoke + время
LAB-02 quick + время
controller quick + время
```

Полезно также записать:

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name,NumberOfCores,NumberOfLogicalProcessors

Get-CimInstance Win32_ComputerSystem |
    Select-Object TotalPhysicalMemory
```

Так мы получим не просто PASS, а воспроизводимый независимый Windows-10
лабораторный стенд.

---

## 15. Что НЕ требуется

Для этой стадии не устанавливать специально:

- Vivado;
- Quartus;
- Gowin IDE;
- Radiant;
- nextpnr;
- FPGA board drivers;
- USB/JTAG drivers.

Мы сначала закрываем pure-RTL correctness.

Только после этого выбирается физическое железо.
