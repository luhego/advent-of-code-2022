from collections import defaultdict


def detect_marker(message, number_of_distinct_letters=4):
    freqs = defaultdict(int)

    start = 0
    for end, _ in enumerate(message):
        freqs[message[end]] += 1

        while freqs[message[end]] > 1:
            freqs[message[start]] -= 1
            if freqs[message[start]] == 0:
                del freqs[message[start]]
            start += 1

        if len(freqs) == number_of_distinct_letters:
            return end + 1


def solution():
    with open("data.in") as f:
        data = f.read().splitlines()

    for line in data:
        # print(detect_marker(line))
        print(detect_marker(line, 14))


solution()
