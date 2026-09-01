#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent

replacements = {
    "ARTICLE_EN.md": [
        ("**Status:** publication manuscript draft v0.9", "**Status:** publication release candidate v1.0"),
        ("5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; preprint arXiv:1701.00141.",
         "5. S. Alikhani, A. Mirjalili, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; preprint arXiv:1701.00141."),
        ("7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.",
         "7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023), 1045–1072. DOI: `10.1007/s10801-022-01214-2`."),
        ("16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.",
         "16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society 58 (2026), e70201. DOI: `10.1112/blms.70201`.")
    ],
    "ARTICLE_RU.md": [
        ("**Статус:** публикационный черновик v0.9", "**Статус:** публикационный релиз-кандидат v1.0"),
        ("5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; arXiv:1701.00141.",
         "5. S. Alikhani, A. Mirjalili, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; arXiv:1701.00141."),
        ("7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.",
         "7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023), 1045–1072. DOI: `10.1007/s10801-022-01214-2`."),
        ("16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.",
         "16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society 58 (2026), e70201. DOI: `10.1112/blms.70201`.")
    ],
}

for src_name, rules in replacements.items():
    src = ROOT / src_name
    text = src.read_text(encoding="utf-8")
    for old, new in rules:
        if old not in text:
            raise SystemExit(f"expected release-normalization string not found in {src_name}: {old[:80]}")
        text = text.replace(old, new)
    out = ROOT / src_name.replace(".md", "_RELEASE.md")
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.name}")
