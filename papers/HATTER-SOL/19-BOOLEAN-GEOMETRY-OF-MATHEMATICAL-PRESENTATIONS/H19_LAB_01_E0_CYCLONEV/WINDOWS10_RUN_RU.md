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


## 6. Новый автоматический physical visibility atlas

Перед реальным Quartus-запуском можно проверить сам анализатор:

~~~powershell
.\tools\test_physical_visibility_atlas.ps1
~~~

Ожидаемый финал:

~~~text
PASS: H19 physical visibility atlas analyzer self-test
~~~

После обычного полного запуска

~~~powershell
.\tools\run_all_cyclonev_a7.ps1
~~~

теперь автоматически формируются три итоговых файла:

~~~text
H19_LAB01_CYCLONEV_SUMMARY.csv
H19_LAB01_PHYSICAL_PARTITIONS.csv
H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md
~~~

Первый содержит сырые сопоставимые физические координаты.

Второй автоматически строит разбиения тройки

~~~text
D = DIRECT12
P = PREFIX19
N = NIELSEN12
~~~

по каждому наблюдателю:

~~~text
ALM
Registers
DSP
Fmax_MHz
DataDelay_ns
LogicLevels
Cell_ns
Routing_ns
~~~

Третий файл уже является научной сводкой H19: в нем фиксируются physical
partitions, joint measured-profile partition, profile-relative latent gap и
вектор видимости DIRECT12/PREFIX19.

Важно: joint measured-profile считается самым тонким только среди реально
извлеченных координат. Он не объявляется полным состоянием Quartus database.

Анализатор также откажется строить atlas, если хотя бы один из трех вариантов
не имеет статуса FIT. Поэтому NOFIT не может случайно попасть в таблицу
routed timing как обычная физическая точка.

## 7. Что прислать после запуска

Теперь достаточно прислать два файла:

~~~text
H19_LAB01_CYCLONEV_SUMMARY.csv
H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md
~~~

Если atlas покажет неожиданное совпадение или резкое расхождение одной
координаты, тогда дополнительно нужен соответствующий worst_path_full.rpt.
