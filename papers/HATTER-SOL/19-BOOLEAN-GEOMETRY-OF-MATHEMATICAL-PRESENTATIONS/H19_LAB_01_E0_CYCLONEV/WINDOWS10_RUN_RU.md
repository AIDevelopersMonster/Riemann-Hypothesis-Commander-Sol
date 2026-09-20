# H19-LAB-01 · Windows 10 / Quartus II 13.1

## 1. Отдельный worktree

Не переключайте существующие H17/H18 каталоги с незакоммиченными
лабораторными файлами.

Из обычного репозитория:

\`\`\`powershell
cd C:\GitHub\Riemann-Hypothesis-Commander-Sol
git fetch origin
git worktree add C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19 origin/research/hatter-sol-19-boolean-geometry
\`\`\`

Затем:

\`\`\`powershell
cd C:\GitHub\Riemann-Hypothesis-Commander-Sol-H19\papers\HATTER-SOL\19-BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS\H19_LAB_01_E0_CYCLONEV
\`\`\`

## 2. Полный matched experiment

\`\`\`powershell
.\tools\run_all_cyclonev_a7.ps1
\`\`\`

Последовательно будут построены:

\`\`\`text
direct12
prefix19
nielsen12
\`\`\`

для одного и того же

\`\`\`text
Cyclone V 5CEFA7F23C6
Quartus II 13.1
100 MHz reference SDC
Slow 1100 mV / 85 C
\`\`\`

После трёх компиляций скрипт автоматически вызывает:

\`\`\`powershell
.\tools\summarize_cyclonev_a7.ps1
\`\`\`

и печатает компактную таблицу:

\`\`\`text
Mode | Fit | ALM | Registers | DSP | Fmax_MHz | DataDelay_ns |
LogicLevels | Cell_ns | Routing_ns
\`\`\`

а также сохраняет:

\`\`\`text
H19_LAB01_CYCLONEV_SUMMARY.csv
\`\`\`

## 3. Один вариант отдельно

Например:

\`\`\`powershell
.\tools\run_cyclonev_a7.ps1 -Mode direct12
\`\`\`

или:

\`\`\`powershell
.\tools\run_cyclonev_a7.ps1 -Mode prefix19
\`\`\`

или:

\`\`\`powershell
.\tools\run_cyclonev_a7.ps1 -Mode nielsen12
\`\`\`

## 4. Что прислать обратно

Достаточно:

\`\`\`text
H19_LAB01_CYCLONEV_SUMMARY.csv
\`\`\`

и, если один из fit/timing результатов выглядит неожиданно, соответствующий

\`\`\`text
worst_path_full.rpt
\`\`\`

Полные Quartus logs нужны только при ошибке или неоднозначном результате.

## 5. Научный вопрос

Этот запуск проверяет survival word физически:

\[
\text{source}
\to
\text{proc/opt}
\to
\text{techmap}
\to
\text{ABC-fast}
\to
\boxed{\text{Cyclone-V P\&R}}.
\]

Особенно важен DIRECT12/PREFIX19:

\[
24>19
\]

на source composition count,

\[
4919=4919
\]

после proc/opt,

\[
63719=63719
\]

после techmap,

но

\[
60374<60383
\]

после ABC-fast.

Quartus покажет, исчезает ли различие снова, сохраняется или меняет знак ещё
раз.
