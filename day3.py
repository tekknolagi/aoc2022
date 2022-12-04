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
        for line in f:
            cmp1, cmp2 = halve(line)
            common = frozenset(cmp1) & frozenset(cmp2)
            assert len(common) == 1
            total_pri += pri(next(iter(common)))
    return total_pri


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
