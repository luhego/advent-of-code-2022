from collections import defaultdict


def max_calories():
    with open("data.in") as f:
        data = f.read().splitlines()

    curr_idx = 0
    calories_by_index = defaultdict(int)
    calories = []
    for line in data:
        if line == "":
            calories.append(calories_by_index[curr_idx])
            curr_idx += 1
            continue
        calories_by_index[curr_idx] += int(line)

    return sorted(calories, reverse=True)


if __name__ == "__main__":
    print(max_calories()[0])
    print(sum(max_calories()[:3]))
