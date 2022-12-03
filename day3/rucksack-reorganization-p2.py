def compute_sum_of_priorities():
    with open("data.in") as f:
        data = f.read().splitlines()

    total = 0
    rucksacks = []
    for rucksack in data:
        rucksacks.append(rucksack)
        if len(rucksacks) == 3:
            total += process_rucksacks_group(rucksacks)
            rucksacks = []

    return total


def process_rucksacks_group(rucksacks):
    total = 0
    common = (set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])).pop()
    if common.islower():
        total += ord(common) - 96
    else:
        total += ord(common) - 38
    return total


if __name__ == "__main__":
    print(compute_sum_of_priorities())
