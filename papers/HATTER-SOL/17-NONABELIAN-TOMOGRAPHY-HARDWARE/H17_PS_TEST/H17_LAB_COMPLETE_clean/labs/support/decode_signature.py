#!/usr/bin/env python3
"""Decode one H17 robust8 24-bit signature into eight 3-bit class fields."""

import sys

WORDS = ("AAB", "Abb", "AAAB", "Abbb", "AABAb", "AAbAb", "ABABB", "ABaBB")
CLASS = {
    0: "1A",
    1: "2A",
    2: "3A",
    3: "4A",
    4: "7A",
    5: "7B",
    6: "RESERVED",
    7: "ERASED/INVALID",
}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: decode_signature.py HEX24  (example: 8d256a)")

    token = sys.argv[1].lower().removeprefix("0x")
    if len(token) > 6:
        raise SystemExit("signature must fit in 24 bits")

    value = int(token, 16)
    if value >= (1 << 24):
        raise SystemExit("signature must fit in 24 bits")

    print(f"signature = {value:06x}")
    print("idx word   bits code class")
    print("--- ------ ---- ---- -------------")

    codes = []
    for i, word in enumerate(WORDS):
        shift = 21 - 3 * i
        code = (value >> shift) & 0x7
        codes.append(code)
        print(f"{i:>3} {word:<6} {code:03b}   {code:>2} {CLASS[code]}")

    print("codes =", ",".join(map(str, codes)))


if __name__ == "__main__":
    main()
