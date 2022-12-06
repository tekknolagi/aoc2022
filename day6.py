import argparse
from collections import deque


def main(args):
    n = 14
    last_n = deque([], maxlen=n)
    idx = 0
    with open(args.file, "r") as f:
        while (c := f.read(1)) != "":
            last_n.append(c)
            idx += 1
            if len(last_n) == n and len(frozenset(last_n)) == n:
                return idx
    raise Exception("could not find start of packet")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
