def contains(interval_1, interval_2):
    return interval_1[0] <= interval_2[0] and interval_1[1] >= interval_2[1]


def find_fully_contained_assigments():
    with open("data.in") as f:
        data = f.read().splitlines()

    count = 0

    for line in data:
        assignment_1, assignment_2 = line.split(",")
        interval_1 = list(map(int, assignment_1.split("-")))
        interval_2 = list(map(int, assignment_2.split("-")))

        if contains(interval_1, interval_2) or contains(interval_2, interval_1):
            count += 1

    return count


def overlap(interval_1, interval_2):
    return (interval_1[0] <= interval_2[1] and interval_1[1] >= interval_2[0]) or (
        interval_2[0] <= interval_1[1] and interval_2[1] >= interval_1[0]
    )


def find_overlapping_assigments():
    with open("data.in") as f:
        data = f.read().splitlines()

    count = 0

    for line in data:
        assignment_1, assignment_2 = line.split(",")
        interval_1 = list(map(int, assignment_1.split("-")))
        interval_2 = list(map(int, assignment_2.split("-")))

        if overlap(interval_1, interval_2):
            count += 1

    return count


# part 1
print(find_fully_contained_assigments())
# part 2
print(find_overlapping_assigments())
