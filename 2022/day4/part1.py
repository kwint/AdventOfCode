def test():
    data = open("input_test", "r").readlines()

    result = main(data)
    print(f"test result: {result}")
    result == 2


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

        if (first_0 >= second_0 and first_1 <= second_1) or (
            second_0 >= first_0 and second_1 <= first_1
        ):
            count += 1
            continue

    return count


if __name__ == "__main__":
    test()
    prod()
