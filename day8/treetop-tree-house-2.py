def top_score(row, col, grid):
    count = 0
    for r in range(row - 1, -1, -1):
        if grid[r][col] >= grid[row][col]:
            count += 1
            break
        count += 1

    return count


def bottom_score(row, col, grid):
    nrows = len(grid)
    count = 0
    for r in range(row + 1, nrows):
        if grid[r][col] >= grid[row][col]:
            count += 1
            break
        count += 1

    return count


def left_score(row, col, grid):
    count = 0
    for c in range(col - 1, -1, -1):
        if grid[row][c] >= grid[row][col]:
            count += 1
            break
        count += 1

    return count


def right_score(row, col, grid):
    ncols = len(grid[0])
    count = 0
    for c in range(col + 1, ncols):
        if grid[row][c] >= grid[row][col]:
            count += 1
            break
        count += 1

    return count


def compute_score(row, col, grid):
    return (
        top_score(row, col, grid)
        * bottom_score(row, col, grid)
        * left_score(row, col, grid)
        * right_score(row, col, grid)
    )


def find_max_score():
    grid = []
    with open("data.in") as f:
        data = f.read().splitlines()

        for line in data:
            row = list(map(int, list(line)))
            grid.append(row)

    nrows = len(grid)
    ncols = len(grid[0])

    max_score = 0
    for row in range(nrows):
        for col in range(ncols):
            score = compute_score(row, col, grid)
            max_score = max(max_score, score)

    return max_score


print(find_max_score())
