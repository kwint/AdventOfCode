MARKER_LENGTH = 14 # 4 for part 1

def test():

    assert main("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert main("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert main("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert main("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    


def prod():
    data = open("input", "r").read()

    result = main(data)
    print(f"prod result: {result}")


def main(data: list):

    for i in range(len(data)):
        chars = data[i:i+MARKER_LENGTH]
        print(chars, len(set(list(chars))))
        if len(set(list(chars))) == MARKER_LENGTH:
            result = i+MARKER_LENGTH
            break

    print(data, result)
    return result


if __name__ == "__main__":
    test()
    prod()
