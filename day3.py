import argparse


def halve(s):
    return (s[: len(s) // 2], s[len(s) // 2 :])


def pri(item):
    if "a" <= item <= "z":
        # starts at 1, not 0
        return ord(item) - ord("a") + 1
    if "A" <= item <= "Z":
        # starts at 27, not 0
        return ord(item) - ord("A") + 27
    raise Exception("UNREACHABLE")


def main(args):
    total_pri = 0
    with open(args.file, "r") as f:
        while True:
            elf1 = f.readline().strip()
            if not elf1:
                break
            elf2 = f.readline().strip()
            elf3 = f.readline().strip()
            common = frozenset(elf1) & frozenset(elf2) & frozenset(elf3)
            assert (
                len(common) == 1
            ), f"unexpected commonalities {common} in {elf1!r}, {elf2!r}, {elf3!r}"
            total_pri += pri(next(iter(common)))
    return total_pri


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
