# HATTER-SOL-19

# Руководство по воспроизведению FPGA-лабораторий H19

Автор: Alex Malachevsky  
ORCID: 0009-0008-6009-3196  
AI research collaborator: Commander Sol · Hatter Sol  
Дата: 20 сентября 2026 г.

## 1. Назначение

Этот документ позволяет независимо повторить две физические лаборатории статьи HATTER-SOL-19:

- H19-LAB-01: Cyclone V / Quartus II 13.1;
- H19-LAB-02: Gowin GW5A-25A / Gowin Education IDE 1.9.9Beta-4.

Сравниваются три E0-эквивалентных presentation:

- DIRECT12;
- PREFIX19;
- NIELSEN12.

Воспроизводится не программирование конкретной платы как обязательный этап, а synthesis/place-and-route/timing/bitstream flow для замороженных target devices. Для проверки основных результатов статьи достаточно корректной установки соответствующего FPGA toolchain.

## 2. Репозиторий

Основной репозиторий:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol

Рабочая ветка H19:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry

Каталог H19:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS

Каталог всей программы HATTER-SOL:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL

## 3. Необходимые программы

### Общие

1. Windows 10/11.
2. Git.
3. PowerShell 5+ / Windows PowerShell.
4. Python 3, доступный как:

~~~powershell
py -3
~~~

Python используется runner-скриптами для генерации замороженного RTL.

### Для Cyclone-V лаборатории

5. Intel/Altera Quartus II 13.1.

Замороженные пути runner:

~~~text
C:\altera\13.1\quartus\bin64\quartus_sh.exe
C:\altera\13.1\quartus\bin64\quartus_sta.exe
~~~

Target:

~~~text
Cyclone V
5CEFA7F23C6
~~~

### Для Gowin лаборатории

6. Gowin Education IDE 1.9.9Beta-4.

Замороженный путь runner:

~~~text
C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe
~~~

Target:

~~~text
Sipeed Tang Primer 25K
GW5A-25A
GW5A-LV25MG121NC1/I0
~~~

Практическая проверенная справка по Gowin CLI:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/GOWIN_CLI_REFERENCE_RU.md

## 4. Получение исходников

Рекомендуется отдельный worktree, чтобы не переключать существующие H17/H18 каталоги.

~~~powershell
cd C:\GitHub\Riemann-Hypothesis-Commander-Sol
git fetch origin
git worktree add C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19 origin/research/hatter-sol-19-boolean-geometry
~~~

После этого H19 находится здесь:

~~~text
C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19\
  papers\HATTER-SOL\
  19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS\
~~~

Если ветка уже checkout локально, достаточно обычного:

~~~powershell
git pull
~~~

## 5. Что генерируют лаборатории

Runner-скрипты не требуют вручную копировать Verilog.

Они вызывают:

~~~text
H17/tools/generate_psl27_closure_classifiers.py
H19/tools/generate_h19_r12_variants.py
~~~

и автоматически строят presentation-specific generated RTL для:

~~~text
direct12
prefix19
nielsen12
~~~

Именно поэтому рекомендуется запускать лабораторию из целого repository/worktree, а не скачивать один PowerShell-файл отдельно.

## 6. H19-LAB-01: Cyclone V

Каталог:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV

Runner всех трёх presentation:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools/run_all_cyclonev_a7.ps1

Runner одного presentation:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools/run_cyclonev_a7.ps1

Summary parser:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools/summarize_cyclonev_a7.ps1

Physical-atlas analyzer:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools/analyze_physical_visibility_atlas.ps1

Provenance hash builder:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools/build_provenance_manifest.ps1

Подробная Windows-инструкция:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/WINDOWS10_RUN_RU.md

### 6.1 Полный запуск

~~~powershell
cd C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19\papers\HATTER-SOL\19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS\H19_LAB_01_E0_CYCLONEV
.\tools\run_all_cyclonev_a7.ps1
~~~

Скрипт последовательно выполняет:

~~~text
direct12
prefix19
nielsen12
~~~

на одном target:

~~~text
5CEFA7F23C6
Quartus II 13.1
100 MHz SDC
Slow 1100 mV / 85 C timing condition
~~~

После трёх run автоматически вызываются summary и physical visibility atlas.

### 6.2 Запуск одного варианта

~~~powershell
.\tools\run_cyclonev_a7.ps1 -Mode direct12
.\tools\run_cyclonev_a7.ps1 -Mode prefix19
.\tools\run_cyclonev_a7.ps1 -Mode nielsen12
~~~

### 6.3 Самотест atlas analyzer

~~~powershell
.\tools\test_physical_visibility_atlas.ps1
~~~

Ожидаемый конец:

~~~text
PASS: H19 physical visibility atlas analyzer self-test
~~~

### 6.4 Итоговые файлы

После полного run должны быть получены:

~~~text
H19_LAB01_CYCLONEV_SUMMARY.csv
H19_LAB01_PHYSICAL_PARTITIONS.csv
H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md
~~~

После provenance step:

~~~powershell
.\tools\build_provenance_manifest.ps1
~~~

получаются:

~~~text
H19_LAB01_PROVENANCE_SHA256.csv
H19_LAB01_PROVENANCE_SHA256.md
~~~

Эталонные committed evidence-файлы:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV

### 6.5 Эталонный результат

На опубликованном run:

~~~text
DIRECT12  ALM=10627  Reg=69  DSP=48  Fmax=28.52 MHz
PREFIX19  ALM=10627  Reg=69  DSP=48  Fmax=28.52 MHz
NIELSEN12 ALM=12017  Reg=69  DSP=48  Fmax=27.50 MHz
~~~

Joint measured physical partition:

~~~text
{{DIRECT12,PREFIX19},{NIELSEN12}}
~~~

## 7. H19-LAB-02: Gowin GW5A-25A

Каталог:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25

Synthesis runner:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools/run_gowin_syn.ps1

P&R runner:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools/run_gowin_pnr.ps1

Synthesis family summarizer:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools/summarize_all_gowin_syn.ps1

P&R family summarizer:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools/summarize_all_gowin_pnr.ps1

Provenance builder:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/blob/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools/build_provenance_manifest.ps1

### 7.1 Проверка Gowin CLI

~~~powershell
& "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe"
~~~

В интерактивной console можно проверить target:

~~~tcl
set_device GW5A-LV25MG121NC1/I0
~~~

Ожидаемый ответ:

~~~text
current device: GW5A-25A  GW5A-LV25MG121NC1/I0
~~~

### 7.2 Synthesis-only calibration

~~~powershell
cd C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19\papers\HATTER-SOL\19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS\H19_LAB_02_E0_GOWIN_GW5A25

.\tools\run_gowin_syn.ps1 -Mode direct12
.\tools\run_gowin_syn.ps1 -Mode prefix19
.\tools\run_gowin_syn.ps1 -Mode nielsen12

.\tools\summarize_all_gowin_syn.ps1
~~~

Эталонный synthesis quotient:

~~~text
{{DIRECT12,PREFIX19},{NIELSEN12}}
~~~

### 7.3 Полный P&R

~~~powershell
.\tools\run_gowin_pnr.ps1 -Mode direct12
.\tools\run_gowin_pnr.ps1 -Mode prefix19
.\tools\run_gowin_pnr.ps1 -Mode nielsen12

.\tools\summarize_all_gowin_pnr.ps1
~~~

Runner фиксирует:

~~~tcl
set_device GW5A-LV25MG121NC1/I0
set_option -top_module h18_r12_comb_controller
set_option -verilog_std sysv2017
set_option -gen_text_timing_rpt 1
set_option -timing_driven 1
set_option -use_mspi_as_gpio 1
set_option -use_ready_as_gpio 1
run all
~~~

Clock constraint:

~~~tcl
create_clock -name clk -period 10.000 [get_ports {clk}]
~~~

Dual-purpose MSPI и READY pins разрешены как GPIO потому, что frozen interface содержит 71 I/O port. Это package-fit configuration, а не изменение RTL semantics.

### 7.4 Итоговые файлы

Synthesis:

~~~text
H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.csv
H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.md
~~~

Post-P&R:

~~~text
H19_LAB02_GOWIN_PNR_SUMMARY.csv
H19_LAB02_GOWIN_PNR_SUMMARY.md
~~~

Provenance:

~~~powershell
.\tools\build_provenance_manifest.ps1
~~~

создаёт:

~~~text
H19_LAB02_GOWIN_PROVENANCE_SHA256.csv
H19_LAB02_GOWIN_PROVENANCE_SHA256.md
~~~

Эталонные committed evidence-файлы находятся в том же LAB-02 каталоге GitHub.

### 7.5 Эталонный post-P&R результат

~~~text
DIRECT12  Logic=19628 LUT=18882 ALU=746 Reg=69 CLS=10150 DSP=28 Fmax=16.276 MHz
PREFIX19  Logic=19628 LUT=18882 ALU=746 Reg=69 CLS=10150 DSP=28 Fmax=16.276 MHz
NIELSEN12 Logic=21448 LUT=20729 ALU=719 Reg=69 CLS=10941 DSP=28 Fmax=16.599 MHz
~~~

Joint measured post-P&R partition:

~~~text
{{DIRECT12,PREFIX19},{NIELSEN12}}
~~~

Все три P&R run завершились успешно, но ни один не закрыл 100 MHz constraint. Поэтому:

~~~text
P&R PASS != timing closure at 100 MHz
~~~

## 8. Что проверять при независимом воспроизведении

Не требуется точного совпадения каждого runtime или временной метки.

Для строгого повторения конкретного frozen experiment проверяются:

1. тот же repository revision;
2. тот же presentation mode;
3. тот же target part;
4. тот же tool/version;
5. тот же 100 MHz constraint;
6. те же runner options;
7. функциональный generation path не изменён;
8. generated summaries получены автоматическими parser scripts;
9. provenance manifest построен после run.

Особенно важно не смешивать:

~~~text
равенство summary coordinates
и
равенство full routed state.
~~~

Статья утверждает первое, но не второе.

## 9. Быстрая проверка результата статьи

Финальная cross-vendor проверка состоит в сравнении двух partition:

~~~text
Cyclone V: {{D,P},{N}}
Gowin:     {{D,P},{N}}
~~~

При этом generic ABC-fast observer ранее давал:

~~~text
{{D},{P},{N}}
~~~

Именно это является центральным H19 observation: presentation distinction может быть видим в одном compiler observer и скрыт в двух независимых physical observers.

## 10. Где брать скрипты

Ничего из лаборатории не требуется копировать из текста статьи.

Все scripts должны браться непосредственно из репозитория:

Cyclone V tools:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_01_E0_CYCLONEV/tools

Gowin tools:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/H19_LAB_02_E0_GOWIN_GW5A25/tools

H19 generators:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS/tools

H17 generator dependency:

https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/research/hatter-sol-19-boolean-geometry/papers/HATTER-SOL/17-NONABELIAN-TOMOGRAPHY-HARDWARE/tools

## 11. Архивируемая evidence map

Для проверки уже выполненного experiment без повторной компиляции используются committed compact evidence:

Cyclone V:

- H19_LAB01_CYCLONEV_SUMMARY.csv;
- H19_LAB01_PHYSICAL_PARTITIONS.csv;
- H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md;
- H19_LAB01_PROVENANCE_SHA256.csv;
- H19_LAB01_PROVENANCE_SHA256.md.

Gowin:

- H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.csv;
- H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.md;
- H19_LAB02_GOWIN_PNR_SUMMARY.csv;
- H19_LAB02_GOWIN_PNR_SUMMARY.md;
- H19_LAB02_GOWIN_PROVENANCE_SHA256.csv;
- H19_LAB02_GOWIN_PROVENANCE_SHA256.md.

## 12. Минимальная последовательность для нового исследователя

~~~text
1. Clone repository.
2. Checkout research/hatter-sol-19-boolean-geometry.
3. Install Python 3 and the desired FPGA toolchain.
4. Enter LAB-01 or LAB-02 directory.
5. Run the frozen presentation scripts for D/P/N.
6. Run the family summarizer.
7. Build the SHA-256 provenance manifest.
8. Compare the induced partition with the committed evidence.
~~~

Если цель - воспроизвести только один physical backend, достаточно соответствующей лаборатории. Для полного центрального результата H19 требуются обе.
