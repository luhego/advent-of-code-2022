def check_top(row, col, grid):
    for r in range(0, row):
        if grid[r][col] >= grid[row][col]:
            return False
    return True


def check_bottom(row, col, grid):
    nrows = len(grid)
    for r in range(row + 1, nrows):
        if grid[r][col] >= grid[row][col]:
            return False
    return True


def check_left(row, col, grid):
    for c in range(0, col):
        if grid[row][c] >= grid[row][col]:
            return False
    return True


def check_right(row, col, grid):
    ncols = len(grid[0])
    for c in range(col + 1, ncols):
        if grid[row][c] >= grid[row][col]:
            return False
    return True


def is_visible(row, col, grid):
    nrows = len(grid)
    ncols = len(grid[0])

    if row == 0 or row == nrows - 1 or col == 0 or col == ncols - 1:
        return True

    # Check top
    if (
        check_top(row, col, grid)
        or check_bottom(row, col, grid)
        or check_left(row, col, grid)
        or check_right(row, col, grid)
    ):
        return True

    return False


def count_visible_trees():
    grid = []
    with open("data.in") as f:
        data = f.read().splitlines()

        for line in data:
            row = list(map(int, list(line)))
            grid.append(row)

    visible_trees = 0

    nrows = len(grid)
    ncols = len(grid[0])

    for row in range(nrows):
        for col in range(ncols):
            if is_visible(row, col, grid):
                visible_trees += 1

    return visible_trees


print(count_visible_trees())
