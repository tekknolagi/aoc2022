import argparse


def overlaps(left, right):
    return left[0] <= right[0] and right[0] <= left[1]


def main(args):
    total = 0
    with open(args.file, "r") as f:
        for pair in f:
            left_range, right_range = pair.strip().split(",")
            left_range = (*map(int, left_range.split("-")),)
            right_range = (*map(int, right_range.split("-")),)
            if overlaps(left_range, right_range) or overlaps(right_range, left_range):
                total += 1
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
