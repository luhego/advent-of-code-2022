def compute_total_signal_strength():
    with open("data.in") as f:
        data = f.read().splitlines()

    X = 1
    cycle = 1
    total_signal_strength = 0
    for line in data:
        args = line.split(" ")
        command = args[0]

        if command == "noop":
            if cycle in [20, 60, 100, 140, 180, 220]:
                total_signal_strength += cycle * X
            cycle += 1
        elif command == "addx":
            value = int(args[1])
            for _ in range(2):
                if cycle in [20, 60, 100, 140, 180, 220]:
                    total_signal_strength += cycle * X
                cycle += 1

            X += value

    return total_signal_strength


print(compute_total_signal_strength())
