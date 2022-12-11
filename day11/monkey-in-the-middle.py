import math

monkeys = []


def show_monkeys():
    for monkey in monkeys:
        print(monkey.starting_items)
    print()


class Monkey:
    def __init__(
        self, monkey_index, starting_items, operation, test, true_monkey, false_monkey
    ) -> None:
        self.monkey_index = monkey_index
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def evaluate(self, first_operator, second_operator, operator):
        if operator == "+":
            return first_operator + second_operator
        elif operator == "*":
            return first_operator * second_operator

    def run(self, div_by_3, k):
        for old_value in self.starting_items:
            self.inspections += 1
            first_operator = (
                old_value if self.operation[0] == "old" else int(self.operation[0])
            )
            second_operator = (
                old_value if self.operation[2] == "old" else int(self.operation[2])
            )
            new_value = self.evaluate(
                first_operator, second_operator, self.operation[1]
            )

            new_value = new_value // 3 if div_by_3 else new_value % k

            if new_value % self.test == 0:
                monkeys[self.true_monkey].starting_items.append(new_value)
            else:
                monkeys[self.false_monkey].starting_items.append(new_value)
        self.starting_items = []


def process_monkey_data(lines):
    monkey_index = int(lines[0].split(" ")[1].split(":")[0])
    starting_items = list(map(int, lines[1].split(":")[1].strip().split(", ")))
    operation = lines[2].split(":")[1].strip().split("=")[1].strip().split(" ")
    test = int(lines[3].split("divisible by ")[1].strip())
    true_monkey = int(lines[4].split("throw to monkey ")[1].strip())
    false_monkey = int(lines[5].split("throw to monkey ")[1].strip())

    return Monkey(
        monkey_index=monkey_index,
        starting_items=starting_items,
        operation=operation,
        test=test,
        true_monkey=true_monkey,
        false_monkey=false_monkey,
    )


def solution(rounds, div_by_3):
    monkeys.clear()
    with open("data.in") as f:
        lines = f.read().splitlines()

    block_size = 7
    i = 0
    for i in range(i, len(lines), block_size):
        monkeys.append(process_monkey_data(lines[i : i + block_size]))

    k = math.prod(monkey.test for monkey in monkeys)
    for i in range(rounds):
        for monkey in monkeys:
            monkey.run(div_by_3, k)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]


print(solution(1, div_by_3=True))
print(solution(10000, div_by_3=False))
