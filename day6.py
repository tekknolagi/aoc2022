import argparse
from collections import deque


def main(args):
    last_four = deque([], maxlen=4)
    idx = 0
    with open(args.file, "r") as f:
        while (c := f.read(1)) != "":
            last_four.append(c)
            idx += 1
            if len(last_four) == 4 and len(frozenset(last_four)) == 4:
                return idx
    raise Exception("could not find start of packet")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
