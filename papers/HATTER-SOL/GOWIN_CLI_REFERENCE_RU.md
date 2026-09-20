# GOWIN CLI / Tcl — практическая справка для HATTER-SOL

Статус: WORKING REFERENCE / VERIFIED-ON-HOST + OFFICIAL-DOC CROSS-CHECK

Дата фиксации: 2026-09-20

Эта справка предназначена для воспроизводимых FPGA-лабораторий HATTER-SOL и
для обычной работы с Gowin EDA из Windows/PowerShell без GUI.

Главное правило: различать

1. команды, **проверенные на реальной локальной установке**;
2. команды, документированные GOWIN, но ещё не проверенные в конкретной версии;
3. синтаксис, который встречается в других FPGA Tcl-flow, но **не работает**
   в проверенной установке Gowin.

---

## 1. Проверенная установка

Хост:

- Windows 10;
- Gowin Education IDE;
- каталог установки:
  `C:\Gowin\Gowin_V1.9.9Beta-4_Education`;
- CLI:
  `C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe`.

Windows version resources у `gw_sh.exe` в этой сборке не заполнены:
`FileVersion`, `ProductVersion`, `FileDescription` возвращаются пустыми.
Версию поэтому следует фиксировать по каталогу установки и, при необходимости,
по release/package metadata, а не по PE VersionInfo.

Запуск из PowerShell:

~~~powershell
& "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe"
~~~

Проверенный banner:

~~~text
*** GOWIN Tcl Command Line Console  ***
%
~~~

Официальный SUG1220 также описывает `gw_sh.exe` как вход в command-line Tcl
mode. Без аргумента открывается интерактивная консоль; с Tcl-файлом выполняется
скрипт.

Пример batch-запуска:

~~~powershell
& "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe" .\flow.tcl
~~~

---

## 2. Важная ловушка: create_project

В проверенной Gowin Education 1.9.9Beta-4 команда

~~~tcl
create_project ...
~~~

**не существует**.

Фактически проверенный ответ:

~~~text
invalid command name "create_project"
~~~

Не переносить автоматически Vivado-подобный Tcl-синтаксис в Gowin.

Практический Gowin-flow строится командами вида

~~~text
set_device
add_file
set_option
run
~~~

а проектный Tcl можно сохранять командой `saveto`, документированной SUG1220.

---

## 3. set_device — выбор FPGA

Проверено локально.

Помощь:

~~~tcl
set_device -h
~~~

Синтаксис локальной версии:

~~~text
set_device [options] <part number>

Options:
  -h, --help
  -name <name>
  -device_version <device_version>
~~~

Проверенный target Tang Primer 25K:

~~~tcl
set_device GW5A-LV25MG121NC1/I0
~~~

Локальная Gowin Education принимает его и сообщает:

~~~text
current device: GW5A-25A  GW5A-LV25MG121NC1/I0
~~~

Следовательно для H19-LAB-02 frozen target:

~~~text
device family/name: GW5A-25A
full part number:   GW5A-LV25MG121NC1/I0
package:            MG121 / MBGA121-class board target
speed/grade suffix: C1/I0
board:              Sipeed Tang Primer 25K
~~~

Не сокращать part number в воспроизводимом flow без необходимости.

---

## 4. add_file — добавление исходников и constraints

Проверено локально.

~~~tcl
add_file -h
~~~

Синтаксис:

~~~text
add_file [options] <file...>

Options:
  -h, --help
  -type <type>
  -disable
~~~

Gowin сам определяет тип по расширению. Официальный SUG1220 перечисляет, в
частности, Verilog, VHDL, SystemVerilog, CST, SDC, GAO/GPA/GSC.

Примеры:

~~~tcl
add_file ./rtl/top.sv
add_file ./rtl/a.sv ./rtl/b.sv ./rtl/top.sv
add_file -type sv ./rtl/top.sv
add_file ./constraints/top.sdc
add_file ./constraints/top.cst
~~~

Официальный manual допускает абсолютные и относительные пути и оба разделителя
`/` и `\`. В command-line mode относительный путь считается относительно
каталога, из которого запущен `gw_sh`.

Для воспроизводимых HATTER-SOL flow предпочтительны либо абсолютные пути,
сгенерированные wrapper-скриптом, либо заранее фиксированный working directory.

---

## 5. set_option — параметры проекта

Проверено локально командой

~~~tcl
set_option -h
~~~

### 5.1 Базовые параметры

~~~text
-output_base_name <name>
-synthesis_tool <tool>
-top_module <name>
-include_path <path>
-verilog_std <v1995|v2001|sysv2017>
-vhdl_std <vhd1993|vhd2008>
-frequency <value>
~~~

Для SystemVerilog HATTER-SOL:

~~~tcl
set_option -top_module h18_r12_comb_controller
set_option -verilog_std sysv2017
set_option -output_base_name h19_direct12_gw5a25
~~~

В локальной версии имеется `-frequency <value>`. Перед использованием как
строгого timing contract следует отдельно проверить его семантику на отчёте и
не подменять им SDC без верификации.

В актуальной документации Gowin также встречается проектная/global frequency
настройка; конкретное имя option зависит от версии, поэтому **локальный
`set_option -h` является главным источником истины для установленной сборки**.

### 5.2 Synthesis controls

Локально доступны:

~~~text
-print_all_synthesis_warning <0|1>
-allow_duplicate_modules <0|1>
-auto_constraint_io <0|1>
-compiler_compatible <0|1>
-default_enum_encoding <default|onehot|gray|sequential>
-disable_io_insertion <0|1>
-fix_gated_and_generated_clocks <0|1>
-looplimit <value>
-maxfan <value>
-multi_file_compilation_unit <0|1>
-num_critical_paths <value>
-num_startend_points <value>
-pipe <0|1>
-resolve_multiple_driver <0|1>
-resource_sharing <0|1>
-retiming <0|1>
-run_prop_extract <0|1>
-rw_check_on_ram <0|1>
-supporttypedflt <0|1>
-symbolic_fsm_compiler <0|1>
-synthesis_onoff_pragma <0|1>
-update_models_cp <0|1>
-write_apr_constraint <0|1>
~~~

Для сравнительных лабораторий не менять optimization options между вариантами.

### 5.3 P&R / timing / reports

Локально доступны:

~~~text
-gen_sdf <0|1>
-gen_io_cst <0|1>
-gen_ibis <0|1>
-gen_posp <0|1>
-gen_text_timing_rpt <0|1>
-gen_verilog_sim_netlist <0|1>
-gen_vhdl_sim_netlist <0|1>
-show_init_in_vo <0|1>
-show_all_warn <0|1>
-timing_driven <0|1>
-reg_in_iob <0|1>
-ireg_in_iob <0|1>
-oreg_in_iob <0|1>
-ioreg_in_iob <0|1>
-replicate_resources <0|1>
-cst_warn_to_error <0|1>
-rpt_auto_place_io_info <0|1>
-place_option <0|1|2>
-route_option <0|1|2>
-inc <value>
-bsram_simple_ce <0|1>
-bsram_simple_addr4 <0|1>
-bsram_simple_wre <0|1>
-clock_route_order <0|1>
-route_maxfan <value>
-correct_hold_violation <0|1>
~~~

Для H19 cross-technology atlas особенно важны:

~~~tcl
set_option -gen_text_timing_rpt 1
set_option -timing_driven 1
~~~

Но метрики следует брать из реально созданных отчётов, а не предполагать
названия/формат файлов заранее.

### 5.4 Dedicated/config pins

Локально доступны:

~~~text
-use_jtag_as_gpio <0|1>
-use_sspi_as_gpio <0|1>
-use_mspi_as_gpio <0|1>
-use_ready_as_gpio <0|1>
-use_done_as_gpio <0|1>
-use_reconfign_as_gpio <0|1>
-use_mode_as_gpio <0|1>
-use_i2c_as_gpio <0|1>
-use_cpu_as_gpio <0|1>
~~~

Не менять эти настройки между сравниваемыми вариантами без явной причины.

### 5.5 Bitstream/configuration controls

Локально доступны:

~~~text
-bit_format <txt|bin>
-bit_crc_check <0|1>
-bit_compress <0|1>
-bit_encrypt <0|1>
-bit_encrypt_key <key>
-bit_security <0|1>
-bit_incl_bsram_init <0|1>
-bg_programming <off|jtag|i2c|internal|goconfig|userlogic|i2c_jtag_sspi_qsspi|jtag_sspi_qsspi>
-hotboot <0|1>
-i2c_slave_addr <value>
-secure_mode <0|1>
-loading_rate <value>
-program_done_bypass <0|1>
-wakeup_mode <0|1>
-user_code <default|value>
-power_on_reset_monitor <0|1>
-spi_flash_addr <value>
-multi_boot <0|1>
-multiboot_address_width <24|32>
-multiboot_mode <normal|fast|dual|quad>
-multiboot_spi_flash_address <value>
-mspi_jump <0|1>
-mspijump_address_width <24|32>
-mspijump_mode <normal|fast|dual|quad>
-mspijump_spi_flash_address <value>
-turn_off_bg <0|1>
-merge_jumpbit <0|1>
-vccaux <2.5|3.3>
-vccx <value>
-cmser <0|1>
-cmser_mode <auto|userlogic>
-cmser_checksum <0|1>
-error_detection <0|1>
-error_detection_correction <0|1>
-stop_cmser <0|1>
-osc_div <4|8|16|32>
-error_injection <0|1>
-ext_cclk <0|1>
-ext_cclk_div <value>
-unused_pin <default|open_drain>
~~~

Для synthesis/P&R comparison обычно не нужны; фиксировать их только если flow
доходит до programming image.

---

## 6. run — synthesis и place-and-route

Проверено локально.

~~~tcl
run -h
~~~

Поддерживаемые процессы:

~~~text
run syn
run pnr
run all
~~~

Смысл:

- `syn` — synthesis;
- `pnr` — place & route;
- `all` — весь implementation flow.

Официальный SUG1220 подтверждает тот же набор.

Для первого полного прогона:

~~~tcl
run all
~~~

Для диагностики полезно разделять:

~~~tcl
run syn
run pnr
~~~

чтобы различать synthesis failure и P&R/timing failure.

---

## 7. saveto — сохранить проектный Tcl

Проверено локально на Gowin Education 1.9.9Beta-4.

Синтаксис документации:

~~~tcl
saveto [-all_options] <file>
~~~

Примеры:

~~~tcl
saveto project_snapshot.tcl
saveto -all_options project_snapshot_full.tcl
~~~

Это особенно полезно для provenance: после успешного GUI/CLI setup можно
сохранить фактическое состояние проекта в воспроизводимый Tcl script.

Локально подтверждён help:

~~~text
Brief:
  Export a tcl script, containing current project's design information.
Usage:
  saveto [options] <file>
Arguments:
  <file>  The script file name.
Options:
  -h, --help
  -all_options
~~~

Таким образом синтаксис ниже считается VERIFIED:

~~~tcl
saveto project_snapshot.tcl
saveto -all_options project_snapshot_full.tcl
~~~

---

## 8. Другие официальные проектные команды

SUG1220 перечисляет также:

~~~text
rm_file
run_close / run close
set_file_enable
set_file_prop
source
~~~

Они пока не входят в минимальный H19-LAB-02 flow.

Если команда критична для лаборатории, сначала проверять её локально через
`<command> -h` либо `help`, а затем фиксировать точный синтаксис здесь.

---

## 9. Минимальный Tcl flow для H19-LAB-02

Ниже **шаблон**, а не ещё замороженный финальный runner:

~~~tcl
# H19-LAB-02 / Tang Primer 25K / skeleton

set_device GW5A-LV25MG121NC1/I0

add_file ./generated/psl27_membership_only.sv
add_file ./generated/psl27_member_class_only.sv
add_file ./generated/h18_r12_comb_core.sv
add_file ./generated/h18_r12_comb_controller.sv

set_option -top_module h18_r12_comb_controller
set_option -verilog_std sysv2017
set_option -output_base_name h19_direct12_gw5a25
set_option -gen_text_timing_rpt 1
set_option -timing_driven 1

run all
~~~

До frozen H19-LAB-02 сюда ещё должны быть добавлены:

1. проверенный clock/timing constraint;
2. одинаковые optimization settings для D/P/N;
3. отдельные output directories;
4. parser реальных Gowin utilization/timing reports;
5. provenance hashes;
6. точная фиксация tool/device/options.

---

## 10. Рекомендуемый PowerShell wrapper

Надёжная схема автоматизации:

~~~powershell
$GwSh = "C:\Gowin\Gowin_V1.9.9Beta-4_Education\IDE\bin\gw_sh.exe"

if (!(Test-Path $GwSh)) {
    throw "Gowin gw_sh.exe not found: $GwSh"
}

& $GwSh .\flow.tcl
if ($LASTEXITCODE -ne 0) {
    throw "Gowin flow failed with exit code $LASTEXITCODE"
}
~~~

Не считать отсутствие PowerShell exception доказательством успешного FIT:
финальный runner должен дополнительно проверять отчёты и явный статус
synthesis/P&R.

---

## 11. Правило воспроизводимой сравнительной лаборатории

Для DIRECT12 / PREFIX19 / NIELSEN12 должны оставаться одинаковыми:

- target part number;
- tool installation;
- top module shell;
- input/output contract;
- constraints;
- synthesis options;
- P&R options;
- report extraction;
- observer definitions.

Меняется только presentation-specific generated RTL.

Иначе FPGA-результат перестаёт быть чистым наблюдением presentation geometry.

---

## 12. Быстрая диагностика

### gw_sh не найден в PATH

~~~powershell
Get-Command gw_sh.exe -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty Source
~~~

Поиск стандартной установки:

~~~powershell
Get-ChildItem -Path C:\Gowin -Filter gw_sh.exe -Recurse -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty FullName
~~~

### Проверить поддержку target

~~~tcl
set_device GW5A-LV25MG121NC1/I0
~~~

Ожидаемый для Primer 25K ответ проверенной установки:

~~~text
current device: GW5A-25A  GW5A-LV25MG121NC1/I0
~~~

### Узнать реальный синтаксис своей версии

~~~tcl
set_device -h
add_file -h
set_option -h
run -h
saveto -h
~~~

**Не считать справочник другой версии более авторитетным, чем help реально
установленного инструмента.**

---

## 13. Источники и версия справки

Основной локальный источник:

- интерактивный help `Gowin_V1.9.9Beta-4_Education/IDE/bin/gw_sh.exe`,
  проверенный 2026-09-20.

Официальные источники:

- GOWIN Semiconductor, **Gowin Software Tcl Commands User Guide**, SUG1220;
- официальный documentation database:
  https://www.gowinsemi.com/en/document/main/database/14/
- доступная индексированная редакция SUG1220:
  https://www.gowinsemi.com/upload/database_doc/3262/document/68b8a001a6a92.pdf

На сайте GOWIN в 2026 году публикуется более новая редакция SUG1220, поэтому
при расхождении приоритет для конкретного хоста:

1. `gw_sh <command> -h`;
2. manual, соответствующий установленной версии;
3. текущий online manual.

---

## 14. Что уже проверено экспериментально

| объект | состояние |
| --- | --- |
| запуск `gw_sh.exe` | VERIFIED |
| интерактивная Tcl console | VERIFIED |
| `create_project` | NOT SUPPORTED in tested build |
| `set_device -h` | VERIFIED |
| Primer 25K full PN accepted | VERIFIED |
| `add_file -h` | VERIFIED |
| `set_option -h` | VERIFIED |
| `run -h` | VERIFIED |
| `run syn/pnr/all` syntax | VERIFIED BY LOCAL HELP |
| `saveto` | VERIFIED |
| full H19-LAB-02 synthesis | PENDING |
| full H19-LAB-02 P&R | PENDING |
| timing/utilization parser | PENDING |

Обновлять эту таблицу по мере прохождения H19-LAB-02.
