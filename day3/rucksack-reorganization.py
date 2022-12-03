def compute_sum_of_priorities():
    with open("data.in") as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        length = len(line)
        first_rucksack = line[: length // 2]
        second_rucksack = line[length // 2 :]

        common = (set(first_rucksack) & set(second_rucksack)).pop()
        if common.islower():
            total += ord(common) - 96
        else:
            total += ord(common) - 38

    return total


if __name__ == "__main__":
    print(compute_sum_of_priorities())
