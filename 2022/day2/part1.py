# A: ROCK
# B: PAPER
# C: SCISSORS

# X: ROCK
# Y: PAPER
# Z: SCISSORS

selected_points = {"X": 1, "Y": 2, "Z": 3}

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
        other, me = game.replace("\n", "").split(" ")
        total_points += selected_points[me] + game_points[other + me]

    return total_points


if __name__ == "__main__":
    test()
    prod()
