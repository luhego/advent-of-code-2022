def display_crt(crt):
    for i, row in enumerate(crt):
        print(
            f"Cycle {i * 40 + 1:>3} -> " + "".join(row) + f" <- Cycle {i * 40 + 40:<3}"
        )


def draw_pixel_in_crt(crt, cycle, X):
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    if col in [X - 1, X, X + 1]:
        crt[row][col] = "#"
    else:
        crt[row][col] = "."


def draw_in_crt():
    with open("data.in") as f:
        data = f.read().splitlines()

    nrows = 6
    ncols = 40
    crt = [[" " for _ in range(ncols)] for _ in range(nrows)]

    X = 1
    cycle = 1
    total_signal_strength = 0
    for line in data:
        args = line.split(" ")
        command = args[0]

        if command == "noop":
            draw_pixel_in_crt(crt, cycle, X)
            cycle += 1
        elif command == "addx":
            value = int(args[1])
            for _ in range(2):
                draw_pixel_in_crt(crt, cycle, X)
                cycle += 1

            X += value

    display_crt(crt)

    return total_signal_strength


print(draw_in_crt())
