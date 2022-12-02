from collections import defaultdict


def rock_paper_scissors():
    with open("data.in") as f:
        data = f.read().splitlines()

    total_score = 0
    for line in data:
        p1, p2 = line.split()
        total_score += play_round(p1, p2)

    return total_score


def play_round(p1, p2):
    p1_map = {"A": "rock", "B": "paper", "C": "scissors"}
    p2_map = {"X": "rock", "Y": "paper", "Z": "scissors"}

    shape_scores = {"rock": 1, "paper": 2, "scissors": 3}
    p1 = p1_map[p1]
    p2 = p2_map[p2]
    p2_score = shape_scores[p2]
    if p1 == p2:
        return 3 + p2_score
    elif p1 == "rock":
        if p2 == "scissors":
            return 0 + p2_score
        else:
            return 6 + p2_score
    elif p1 == "paper":
        if p2 == "rock":
            return 0 + p2_score
        else:
            return 6 + p2_score
    elif p1 == "scissors":
        if p2 == "paper":
            return 0 + p2_score
        else:
            return 6 + p2_score


if __name__ == "__main__":
    print(rock_paper_scissors())
