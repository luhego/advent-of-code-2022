def are_next_to_each_other(knot_positions, curr_index):
    pos1 = knot_positions[curr_index - 1]
    pos2 = knot_positions[curr_index]
    if pos1[0] == pos2[0]:
        return abs(pos1[1] - pos2[1]) <= 1
    elif pos1[1] == pos2[1]:
        return abs(pos1[0] - pos2[0]) <= 1
    elif abs(pos1[0] - pos2[0]) == 1 and abs(pos1[1] - pos2[1]) == 1:
        return True
    return False


def move_secondary_knot(knot_positions, curr_index):
    if are_next_to_each_other(knot_positions, curr_index):
        return knot_positions

    prev_position = knot_positions[curr_index - 1]
    curr_position = knot_positions[curr_index]

    if curr_position[0] == prev_position[0]:
        if curr_position[1] < prev_position[1]:
            curr_position = (curr_position[0], curr_position[1] + 1)
        else:
            curr_position = (curr_position[0], curr_position[1] - 1)
    elif curr_position[1] == prev_position[1]:
        if curr_position[0] < prev_position[0]:
            curr_position = (curr_position[0] + 1, curr_position[1])
        else:
            curr_position = (curr_position[0] - 1, curr_position[1])
    else:
        if curr_position[0] < prev_position[0]:
            if curr_position[1] < prev_position[1]:
                curr_position = (curr_position[0] + 1, curr_position[1] + 1)
            else:
                curr_position = (curr_position[0] + 1, curr_position[1] - 1)
        else:
            if curr_position[1] < prev_position[1]:
                curr_position = (curr_position[0] - 1, curr_position[1] + 1)
            else:
                curr_position = (curr_position[0] - 1, curr_position[1] - 1)

    knot_positions[curr_index] = curr_position
    return knot_positions


def move_primary_knot(knot_positions, knot_index, direction, steps, visited):
    if steps == 0:
        return knot_positions

    knot_position = knot_positions[knot_index]
    if direction == "R":
        knot_positions[knot_index] = (knot_position[0], knot_position[1] + 1)
    elif direction == "L":
        knot_positions[knot_index] = (knot_position[0], knot_position[1] - 1)
    elif direction == "U":
        knot_positions[knot_index] = (knot_position[0] - 1, knot_position[1])
    elif direction == "D":
        knot_positions[knot_index] = (knot_position[0] + 1, knot_position[1])

    for i in range(1, len(knot_positions)):
        knot_positions = move_secondary_knot(knot_positions, i)

        if i == len(knot_positions) - 1:
            visited.add(knot_positions[i])

    return move_primary_knot(knot_positions, knot_index, direction, steps - 1, visited)


def simulate_knots_movements(number_of_nots):
    with open("data.in") as f:
        data = f.read().splitlines()

        knots_positions = [(0, 0) for _ in range(number_of_nots)]
        visited = set()
        for line in data:
            direction, steps = line.split(" ")
            steps = int(steps)
            knots_positions = move_primary_knot(
                knots_positions, 0, direction, steps, visited
            )

        return len(visited)


print(simulate_knots_movements(10))
