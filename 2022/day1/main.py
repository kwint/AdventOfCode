def test():
    calories = open("input_test", "r").readlines()

    result = main(calories)
    print(f"test result: {result}")
    result == 45000


def prod():
    calories = open("input", "r").readlines()

    result = main(calories)
    print(f"prod result: {result}")
    # result == 24000


def main(calories: list):

    current_elf = 0
    elfs = []
    print(calories[-1])
    for calorie in calories:
        # print(calorie.replace("\n", ""))
        if calorie == "\n":
            elfs.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(calorie)

    # Also add last elf
    elfs.append(current_elf)

    elfs.sort()
    return sum(elfs[-3:])


if __name__ == "__main__":
    test()
    prod()
