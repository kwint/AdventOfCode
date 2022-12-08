# A: ROCK 1
# B: PAPER 2
# C: SCISSORS 3

# X: ROCK  | LOSE
# Y: PAPER | DRAW
# Z: SCISSORS | WIN

selected_points = {"X": 1, "Y": 2, "Z": 3}
state_points = {"X": 0, "Y": 3, "Z": 6}
game_points = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

to_select = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}


def test():
    calories = open("input_test", "r").readlines()

    result = main(calories)
    print(f"test result: {result}")
    result == 15


def prod():
    calories = open("input", "r").readlines()

    result = main(calories)
    print(f"prod result: {result}")
    # result == 24000


def main(data: list):

    total_points = 0
    for game in data:
        other, state = game.replace("\n", "").split(" ")
        total_points += state_points[state] + to_select[other][state]

    return total_points


if __name__ == "__main__":
    test()
    prod()
