import argparse


def main(args):
    total_calories = []
    with open(args.file, "r") as f:
        current_total = 0
        for line in f:
            if line == "\n":
                total_calories.append(current_total)
                current_total = 0
            else:
                current_total += int(line)
    if current_total > 0:
        # The last group in a file wouldn't have had a blank line after
        total_calories.append(current_total)
    return max(total_calories)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
