import argparse


def normalize_shape(shape):
    return {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }[shape]


def normalize_goal(letter):
    return {
        "X": 1,
        "Y": 0,
        "Z": -1,
    }[letter]


def cmp(opp, you):
    "Return 0 for draw, 1 for opponent win, -1 for you win"
    if opp == you:
        return 0
    if opp == "paper" and you == "rock":
        return 1
    if opp == "rock" and you == "scissors":
        return 1
    if opp == "scissors" and you == "paper":
        return 1
    return -cmp(you, opp)


def score_shape(shape):
    return {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }[shape]


def score(opp, goal):
    "Return a two-tuple of (opp_score, you_score)"
    opp = normalize_shape(opp)
    for move in ("rock", "paper", "scissors"):
        score = cmp(opp, move)
        if score == normalize_goal(goal):
            break
    else:
        raise Exception("UNREACHABLE")
    opp_score = score_shape(opp)
    you_score = score_shape(move)
    if score == 0:
        return (opp_score + 3, you_score + 3)
    if score > 0:
        return (opp_score + 6, you_score)
    if score < 0:
        return (opp_score, you_score + 6)
    raise Exception("UNREACHABLE")


def main(args):
    opp_total = you_total = 0
    with open(args.file, "r") as f:
        for line in f:
            opp, you = line.split()
            opp_score, you_score = score(opp, you)
            opp_total += opp_score
            you_total += you_score
    return (opp_total, you_total)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/dev/stdin")
    args = parser.parse_args()
    print(main(args))
