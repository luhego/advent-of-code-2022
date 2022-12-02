from collections import defaultdict


def rock_paper_scissors():
    with open("data.in") as f:
        data = f.read().splitlines()

    total_score = 0
    for line in data:
        p1, p2 = line.split()
        p2 = get_correct_shape(p1, p2)
        total_score += play_round(p1, p2)

    return total_score


def get_correct_shape(p1, p2):
    # need to lose
    if p2 == "X":
        return {"A": "C", "B": "A", "C": "B"}[p1]

    # need to draw
    elif p2 == "Y":
        return p1

    # need to win
    elif p2 == "Z":
        return {"A": "B", "B": "C", "C": "A"}[p1]


def play_round(p1, p2):
    p_map = {"A": "rock", "B": "paper", "C": "scissors"}

    shape_scores = {"rock": 1, "paper": 2, "scissors": 3}
    p1 = p_map[p1]
    p2 = p_map[p2]
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
