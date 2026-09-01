#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent

configs = {
    "ARTICLE_EN.md": {
        "title_block": "---\ntitle: \"Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra\"\nsubtitle: \"Wreath Coherence, Partition Compression, and Exact Orbital Separation\"\nauthor: \"Alex Malachevsky\"\ndate: \"2026-09-01\"\n---\n\n**Series:** Commander Sol / Fixed-Carrier Oriented Algebra  \n**Status:** publication release candidate v1.0  \n\n---\n",
        "prefix": "# Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra\n## Wreath Coherence, Partition Compression, and Exact Orbital Separation\n\n**Author:** Alex Malachevsky  \n**Series:** Commander Sol / Fixed-Carrier Oriented Algebra  \n**Status:** publication manuscript draft v0.9  \n**Date:** 2026-09-01\n\n---\n",
        "rules": [
            ("5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; preprint arXiv:1701.00141.",
             "5. S. Alikhani, A. Mirjalili, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; preprint arXiv:1701.00141."),
            ("7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.",
             "7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023), 1045–1072. DOI: `10.1007/s10801-022-01214-2`."),
            ("16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.",
             "16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society 58 (2026), e70201. DOI: `10.1112/blms.70201`.")
        ],
    },
    "ARTICLE_RU.md": {
        "title_block": "---\ntitle: \"Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре\"\nsubtitle: \"Wreath-когерентность, сжатие разбиений и точное орбитальное разделение\"\nauthor: \"Alex Malachevsky\"\ndate: \"2026-09-01\"\nlang: ru-RU\n---\n\n**Серия:** Commander Sol / Fixed-Carrier Oriented Algebra  \n**Статус:** публикационный релиз-кандидат v1.0  \n\n---\n",
        "prefix": "# Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре\n## Wreath-когерентность, сжатие разбиений и точное орбитальное разделение\n\n**Автор:** Alex Malachevsky  \n**Серия:** Commander Sol / Fixed-Carrier Oriented Algebra  \n**Статус:** публикационный черновик v0.9  \n**Дата:** 2026-09-01\n\n---\n",
        "rules": [
            ("5. S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; arXiv:1701.00141.",
             "5. S. Alikhani, A. Mirjalili, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, Journal of Information and Optimization Sciences 43 (2022), 311–321. DOI: `10.1080/02522667.2021.2003011`; arXiv:1701.00141."),
            ("7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI: `10.1007/s10801-022-01214-2`.",
             "7. M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023), 1045–1072. DOI: `10.1007/s10801-022-01214-2`."),
            ("16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI: `10.1112/blms.70201`.",
             "16. L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society 58 (2026), e70201. DOI: `10.1112/blms.70201`.")
        ],
    },
}

for src_name, cfg in configs.items():
    src = ROOT / src_name
    text = src.read_text(encoding="utf-8")
    if not text.startswith(cfg["prefix"]):
        raise SystemExit(f"unexpected publication prefix in {src_name}")
    text = cfg["title_block"] + text[len(cfg["prefix"]):]
    for old, new in cfg["rules"]:
        if old not in text:
            raise SystemExit(f"expected release-normalization string not found in {src_name}: {old[:80]}")
        text = text.replace(old, new)
    out = ROOT / src_name.replace(".md", "_RELEASE.md")
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.name}")
