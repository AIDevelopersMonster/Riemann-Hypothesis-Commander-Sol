package require ::quartus::device

puts "=== QUARTUS DEVICE FAMILY PROBE ==="
set families [get_family_list]
set sv_family ""
foreach f $families {
    if {[string equal -nocase $f "Stratix V"]} {
        set sv_family $f
    }
}

if {$sv_family eq ""} {
    puts "STRATIX_V_FAMILY=NOT_INSTALLED"
    puts "Families containing Stratix:"
    foreach f $families {
        if {[string match -nocase "*Stratix*" $f]} {
            puts "  $f"
        }
    }
    exit 2
}

puts "STRATIX_V_FAMILY=INSTALLED"
puts "Family=$sv_family"

set parts [lsort [get_part_list -family $sv_family]]
puts "PART_COUNT=[llength $parts]"

array set seen_device {}
puts "=== UNIQUE DEVICES / FIRST AVAILABLE PART ==="
foreach p $parts {
    set d [get_part_info -device $p]
    if {![info exists seen_device($d)]} {
        set seen_device($d) 1
        set pkg [get_part_info -package $p]
        set pins [get_part_info -pin_count $p]
        set sg [get_part_info -speed_grade $p]
        set tg [get_part_info -temperature_grade $p]
        puts "$d | sample=$p | package=$pkg | pins=$pins | speed=$sg | temp=$tg"
    }
}

puts "=== 5SGXA3 PARTS ==="
set a3_count 0
foreach p $parts {
    set d [get_part_info -device $p]
    if {[string equal $d "5SGXA3"]} {
        incr a3_count
        set pkg [get_part_info -package $p]
        set pins [get_part_info -pin_count $p]
        set sg [get_part_info -speed_grade $p]
        set tg [get_part_info -temperature_grade $p]
        puts "$p | package=$pkg | pins=$pins | speed=$sg | temp=$tg"
    }
}
puts "5SGXA3_PART_COUNT=$a3_count"
