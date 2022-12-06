import argparse
import re


def read_towers(f):
    towers = []
    for line in f:
        if line == "\n":
            break
        items = [line[i : i + 4].strip() for i in range(0, len(line), 4)]
        if not towers:
            for i in range(len(items)):
                towers.append([])
        if any(item.isnumeric() for item in items):
            break
        for idx, item in enumerate(items):
            if item:
                towers[idx].append(item.replace("[", "").replace("]", ""))
    for tower in towers:
        tower.reverse()
    towers.insert(0, None)  # 1-indexed
    return towers


def main(args):
    with open(args.file, "r") as f:
        towers = read_towers(f)
        assert f.readline() == "\n"
        for command in f:
            groups = re.match(r"move (\d+) from (\d+) to (\d+)", command).groups()
            count, from_, to = map(int, groups)
            to_move = towers[from_][-count:]
            del towers[from_][-count:]
            towers[to].extend(to_move)
    return "".join(tower[-1] for tower in towers[1:])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
