def are_next_to_each_other(pos1, pos2):
    if pos1[0] == pos2[0]:
        return abs(pos1[1] - pos2[1]) <= 1
    elif pos1[1] == pos2[1]:
        return abs(pos1[0] - pos2[0]) <= 1
    elif abs(pos1[0] - pos2[0]) == 1 and abs(pos1[1] - pos2[1]) == 1:
        return True
    return False


def move_tail(tail_position, head_position):
    if are_next_to_each_other(head_position, tail_position):
        return tail_position

    if tail_position[0] == head_position[0]:
        if tail_position[1] < head_position[1]:
            tail_position = (tail_position[0], tail_position[1] + 1)
        else:
            tail_position = (tail_position[0], tail_position[1] - 1)
    elif tail_position[1] == head_position[1]:
        if tail_position[0] < head_position[0]:
            tail_position = (tail_position[0] + 1, tail_position[1])
        else:
            tail_position = (tail_position[0] - 1, tail_position[1])
    else:
        if tail_position[0] < head_position[0]:
            if tail_position[1] < head_position[1]:
                tail_position = (tail_position[0] + 1, tail_position[1] + 1)
            else:
                tail_position = (tail_position[0] + 1, tail_position[1] - 1)
        else:
            if tail_position[1] < head_position[1]:
                tail_position = (tail_position[0] - 1, tail_position[1] + 1)
            else:
                tail_position = (tail_position[0] - 1, tail_position[1] - 1)

    return tail_position


def move_head(head_position, tail_position, direction, steps, visited):
    if steps == 0:
        return head_position, tail_position

    if direction == "R":
        head_position = (head_position[0], head_position[1] + 1)
    elif direction == "L":
        head_position = (head_position[0], head_position[1] - 1)
    elif direction == "U":
        head_position = (head_position[0] - 1, head_position[1])
    elif direction == "D":
        head_position = (head_position[0] + 1, head_position[1])

    tail_position = move_tail(tail_position, head_position)

    visited.add(tail_position)

    return move_head(head_position, tail_position, direction, steps - 1, visited)


def solution():
    with open("data.in") as f:
        data = f.read().splitlines()

        tail_position = (0, 0)
        head_position = (0, 0)
        visited = set()
        for line in data:
            direction, steps = line.split(" ")
            steps = int(steps)
            head_position, tail_position = move_head(
                head_position, tail_position, direction, steps, visited
            )

        return len(visited)


print(solution())
