package require ::quartus::device

puts "=== QUARTUS ARRIA V DEVICE PROBE ==="

set families [get_family_list]
set av_families {}
foreach f $families {
    if {[string match -nocase "*Arria V*" $f]} {
        lappend av_families $f
    }
}

if {[llength $av_families] == 0} {
    puts "ARRIA_V=NOT_INSTALLED"
    puts "Arria families visible in this Quartus instance:"
    foreach f $families {
        if {[string match -nocase "*Arria*" $f]} {
            puts "  $f"
        }
    }
    exit 2
}

puts "ARRIA_V=INSTALLED"
puts "Matched families:"
foreach f $av_families {
    puts "  $f"
}

array set seen_device {}
set total_parts 0

foreach f $av_families {
    set parts [lsort [get_part_list -family $f]]
    incr total_parts [llength $parts]

    puts "=== FAMILY: $f | PART_COUNT=[llength $parts] ==="

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
}

puts "TOTAL_PART_COUNT=$total_parts"

puts "=== ALL COMMERCIAL PARTS, FIRST 100 ==="
set shown 0
foreach f $av_families {
    foreach p [lsort [get_part_list -family $f]] {
        set tg [get_part_info -temperature_grade $p]
        if {[string equal -nocase $tg "Commercial"]} {
            set d [get_part_info -device $p]
            set pkg [get_part_info -package $p]
            set pins [get_part_info -pin_count $p]
            set sg [get_part_info -speed_grade $p]
            puts "$p | device=$d | package=$pkg | pins=$pins | speed=$sg | temp=$tg"
            incr shown
            if {$shown >= 100} {
                break
            }
        }
    }
    if {$shown >= 100} {
        break
    }
}
puts "COMMERCIAL_PARTS_SHOWN=$shown"
