$ErrorActionPreference = "Stop"

$Lab = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$OutCsv = Join-Path $Lab "H19_LAB01_PROVENANCE_SHA256.csv"
$OutMd = Join-Path $Lab "H19_LAB01_PROVENANCE_SHA256.md"

$modes = @("direct12","prefix19","nielsen12")
$rows = @()

function Add-HashedFile(
  [string]$Mode,
  [string]$Kind,
  [string]$Path,
  [bool]$Required = $true
) {
  if (!(Test-Path $Path)) {
    if ($Required) {
      throw ("missing required provenance file: {0}" -f $Path)
    }
    return
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
  $project = "h19_" + $mode + "_cv_a7"
  $gen = Join-Path $Lab ("generated\" + $mode)
  $qdir = Join-Path $Lab ("quartus13_cyclonev_a7\" + $mode)
  $out = Join-Path $qdir "output_files"

  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "psl27_membership_only.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "psl27_member_class_only.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "h18_r12_comb_core.sv")
  Add-HashedFile $mode "generated-rtl" (Join-Path $gen "h18_r12_comb_controller.sv")

  Add-HashedFile $mode "quartus-input" (Join-Path $qdir ($project + ".qsf"))
  Add-HashedFile $mode "quartus-input" (Join-Path $qdir ($project + ".sdc"))

  Add-HashedFile $mode "quartus-report" (Join-Path $out ($project + ".fit.rpt"))
  Add-HashedFile $mode "quartus-report" (Join-Path $out ($project + ".map.rpt"))
  Add-HashedFile $mode "quartus-report" (Join-Path $out ($project + ".sta.rpt"))
  Add-HashedFile $mode "quartus-report" (Join-Path $qdir "worst_path_full.rpt")

  Add-HashedFile $mode "quartus-report-optional" (Join-Path $out ($project + ".flow.rpt")) $false
}

$rows | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $OutCsv

$branchName = (& git -C $Lab branch --show-current).Trim()
$head = (& git -C $Lab rev-parse HEAD).Trim()

$lines = @()
$lines += "# H19-LAB-01 · Cyclone-V provenance SHA-256 manifest"
$lines += ""
$lines += "Status: GENERATED FROM LOCAL PHYSICAL RUN ARTIFACTS"
$lines += ""
$lines += ("Manifest-generation branch: " + $branchName)
$lines += ("Manifest-generation HEAD: " + $head)
$lines += "Target: 5CEFA7F23C6"
$lines += "Tool flow: Quartus II 13.1"
$lines += "Hash: SHA-256"
$lines += ""
$lines += "The heavy generated/ and quartus13_cyclonev_a7/ directories are intentionally not tracked."
$lines += "This manifest fingerprints the generated RTL, Quartus project constraints, fitter/map/TimeQuest reports, and routed worst-path report used by the frozen H19-LAB-01 result."
$lines += ""
$lines += "| mode | kind | bytes | SHA-256 | relative path |"
$lines += "| --- | --- | ---: | --- | --- |"

foreach ($r in $rows) {
  $lines += ("| {0} | {1} | {2} | {3} | {4} |" -f $r.Mode,$r.Kind,$r.Bytes,$r.SHA256,$r.RelativePath)
}

$lines += ""
$lines += ("Files fingerprinted: " + $rows.Count)
$lines += ""
$lines += "Claim boundary: hashes certify these local files byte-for-byte; they do not by themselves prove deterministic rerouting across machines or Quartus installations."

$lines | Set-Content -Encoding UTF8 -Path $OutMd

Write-Host ""
Write-Host "== H19-LAB-01 PROVENANCE SHA256 =="
Write-Host ("Files fingerprinted: {0}" -f $rows.Count)
Write-Host ("CSV: {0}" -f $OutCsv)
Write-Host ("Markdown: {0}" -f $OutMd)
Write-Host "PASS: H19-LAB-01 provenance manifest generated"
