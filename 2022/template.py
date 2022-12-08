def test():
    data = open("input_test", "r").readlines()

    result = main(data)
    print(f"test result: {result}")
    result == 0


def prod():
    data = open("input", "r").readlines()

    result = main(data)
    print(f"prod result: {result}")


def main(data: list):

    # DO stuff

    return


if __name__ == "__main__":
    test()
    prod()
