import re

EMPTY = "   "


def parse_instruction(line):
    return list(map(int, re.findall(r"\d+", line)))


def convert_grid_to_stacks(grid):
    rows = len(grid)
    cols = len(grid[0])
    stacks = [[] for _ in range(cols)]

    for row in range(rows - 1, -1, -1):
        for col in range(cols):
            if grid[row][col] != "<EMPTY>":
                stacks[col].append(grid[row][col])

    return stacks


def process_instructions(stacks, instructions, all_at_once=False):
    for instruction in instructions:
        quantity = instruction[0]
        source = instruction[1] - 1
        destination = instruction[2] - 1

        if all_at_once:
            n = len(stacks[source])
            stacks[destination].extend(stacks[source][n - quantity :])
            while quantity:
                stacks[source].pop()
                quantity -= 1
        else:
            while quantity > 0:
                stacks[destination].append(stacks[source].pop())
                quantity -= 1


def preprocess():
    with open("data.in") as f:
        data = f.read().splitlines()

        grid = []
        instructions = []
        for line in data:
            stripped_line = line.strip()
            if "[" in stripped_line:
                row = []
                i = 0
                while i < len(line):
                    block = line[i : i + 3]
                    if block == EMPTY:
                        row.append("<EMPTY>")
                    else:
                        row.append(block[1])
                    i += 4

                grid.append(row)
            elif stripped_line == "":
                continue
            elif stripped_line[0] == "1":
                continue
            else:
                instructions.append(parse_instruction(line))
    stacks = convert_grid_to_stacks(grid)

    return stacks, instructions


def solution():
    stacks, instructions = preprocess()
    process_instructions(stacks, instructions)

    tops = [stack[-1] for stack in stacks]
    return "".join(tops)


def solution2():
    stacks, instructions = preprocess()
    process_instructions(stacks, instructions, all_at_once=True)

    tops = [stack[-1] for stack in stacks]
    return "".join(tops)


# part1
print(solution())
# part2
print(solution2())
