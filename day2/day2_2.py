def main():
    with open("day2/input.txt") as fp:
        lines = fp.readlines()

    assert get_end_pos(lines) == 2086261056


def get_end_pos(lines):
    #               TODO can be cleaner
    instructions = [(cmd, int(x)) for cmd, x in [line.split() for line in lines]]

    aim, hor, depth = 0, 0, 0
    for cmd, x in instructions:
        match cmd:
            case "forward":
                hor += x
                depth += x*aim
            case "up":
                aim -= x
            case "down":
                aim += x

    print(f"{hor=}, {depth=}, {hor * depth=}")
    return hor * depth


def test_get_end_pos():
    lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    assert get_end_pos(lines) == 900


if __name__ == "__main__":
    test_get_end_pos()
    main()
