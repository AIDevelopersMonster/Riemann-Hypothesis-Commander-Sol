$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$OutCsv = Join-Path $Lab "H19_LAB02_GOWIN_PROVENANCE_SHA256.csv"
$OutMd = Join-Path $Lab "H19_LAB02_GOWIN_PROVENANCE_SHA256.md"

$modes = @("direct12","prefix19","nielsen12")
$rows = @()

function Add-HashedFile(
  [string]$Mode,
  [string]$Kind,
  [string]$Path
) {
  if (!(Test-Path $Path)) {
    throw ("missing required provenance file: {0}" -f $Path)
  }

  $item = Get-Item $Path
  $hash = Get-FileHash -Algorithm SHA256 -Path $Path
  $relative = $item.FullName.Substring($Lab.Length).TrimStart("\")
  $script:rows += [pscustomobject]@{
    Mode = $Mode
    Kind = $Kind
    RelativePath = $relative
    Bytes = $item.Length
    SHA256 = $hash.Hash.ToLowerInvariant()
  }
}

foreach ($mode in $modes) {
  $project = "h19_" + $mode + "_gw5a25_pnr"
  $gen = Join-Path $Lab ("generated\" + $mode)
  $work = Join-Path $Lab ("gowin_1_9_9b4_pnr\" + $mode)
  $syn = Join-Path $work "impl\gwsynthesis"
  $pnr = Join-Path $work "impl\pnr"

  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "psl27_membership_only.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "psl27_member_class_only.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "h18_r12_comb_core.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "h18_r12_comb_controller.sv")

  Add-HashedFile $mode "gowin-input" (Join-Path $work ($project + ".sdc"))
  Add-HashedFile $mode "gowin-input" (Join-Path $work ($project + ".tcl"))
  Add-HashedFile $mode "gowin-snapshot" (Join-Path $work ($project + "_snapshot.tcl"))
  Add-HashedFile $mode "gowin-transcript" (Join-Path $work ($project + ".log"))

  Add-HashedFile $mode "gowin-synthesis-report" (Join-Path $syn ($project + "_syn.rpt.html"))
  Add-HashedFile $mode "gowin-pnr-report" (Join-Path $pnr ($project + ".rpt.txt"))
  Add-HashedFile $mode "gowin-timing-report" (Join-Path $pnr ($project + ".tr"))
}

$rows | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $OutCsv

$branchName = (& git -C $Lab branch --show-current).Trim()
$head = (& git -C $Lab rev-parse HEAD).Trim()

$lines = @()
$lines += "# H19-LAB-02 · Gowin GW5A-25A provenance SHA-256 manifest"
$lines += ""
$lines += "Status: GENERATED FROM LOCAL PHYSICAL RUN ARTIFACTS"
$lines += ""
$lines += ("Manifest-generation branch: " + $branchName)
$lines += ("Manifest-generation HEAD: " + $head)
$lines += "Target: GW5A-25A / GW5A-LV25MG121NC1/I0"
$lines += "Tool flow: Gowin Education IDE 1.9.9Beta-4 / gw_sh"
$lines += "Clock contract: clk = 100 MHz, SDC period 10.000 ns"
$lines += "Dual-purpose I/O configuration used for physical fit: MSPI + READY as GPIO"
$lines += "Hash: SHA-256"
$lines += ""
$lines += "The heavy generated/ and gowin_1_9_9b4_pnr/ directories are intentionally not tracked."
$lines += "This manifest fingerprints the generated RTL, explicit SDC/Tcl inputs, saved Gowin option snapshots, primary transcripts, synthesis reports, P&R resource reports, and post-route timing reports used by the frozen H19-LAB-02 result."
$lines += ""
$lines += "| mode | kind | bytes | SHA-256 | relative path |"
$lines += "| --- | --- | ---: | --- | --- |"

foreach ($r in $rows) {
  $lines += ("| {0} | {1} | {2} | {3} | {4} |" -f $r.Mode,$r.Kind,$r.Bytes,$r.SHA256,$r.RelativePath)
}

$lines += ""
$lines += ("Files fingerprinted: " + $rows.Count)
$lines += ""
$lines += "Claim boundary: hashes certify these local files byte-for-byte. They do not prove deterministic placement/routing across machines, tool installations, seeds, or future Gowin versions."

$lines | Set-Content -Encoding UTF8 -Path $OutMd

Write-Host ""
Write-Host "== H19-LAB-02 GOWIN PROVENANCE SHA256 =="
Write-Host ("Files fingerprinted: {0}" -f $rows.Count)
Write-Host ("CSV: {0}" -f $OutCsv)
Write-Host ("Markdown: {0}" -f $OutMd)
Write-Host "PASS: H19-LAB-02 Gowin provenance manifest generated"
