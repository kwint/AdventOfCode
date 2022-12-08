import numpy as np

point_lookup = {
    x: y
    for x, y in zip([chr(letter) for letter in range(97, 97 + 26)], range(1, 1 + 27))
} | {
    x: y
    for x, y in zip([chr(letter) for letter in range(65, 65 + 26)], range(27, 27 + 27))
}


def test():
    data = open("input_test", "r").readlines()

    result = main(data)
    print(f"test result: {result}")
    result == 70


def prod():
    data = open("input", "r").readlines()

    result = main(data)
    print(f"prod result: {result}")


def main(data: list):

    data = [line.replace("\n", "") for line in data]

    common_letters = []
    for main, comp1, comp2 in zip(*[iter(data)] * 3):
        print(f"{main=}, {comp1=}, {comp2=}")

        common = [letter for letter in main if letter in comp1 and letter in comp2]
        assert len(np.unique(common)) == 1, f"More than one common letter {common}"
        common_letters.append(common[0])

    print(common_letters)
    return sum(point_lookup[x] for x in common_letters)


if __name__ == "__main__":
    test()
    prod()
