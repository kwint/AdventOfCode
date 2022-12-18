def test():
    data = open("input_test", "r").readlines()

    result = main(data)
    print(f"test result: {result}")
    result == 4


def prod():
    data = open("input", "r").readlines()

    result = main(data)
    print(f"prod result: {result}")


def main(data: list):

    count = 0
    for pair in data:
        first, second = pair.split(",")
        first_0, first_1 = [int(x) for x in first.split("-")]
        second_0, second_1 = [int(x) for x in second.split("-")]
        first = list(range(first_0, first_1 + 1))
        second = list(range(second_0, second_1 + 1))

        if any(x in second for x in first) or any(x in first for x in second):
            count += 1

    return count


if __name__ == "__main__":
    test()
    prod()
