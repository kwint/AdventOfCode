def main():
    with open("day2/input.txt") as fp:
        lines = fp.readlines()

    assert get_end_pos(lines) == 2091984


def get_end_pos(lines):
    instructions = [(cmd, int(x)) for cmd, x in [line.split() for line in lines]]
    hor = sum(x for dr, x in instructions if dr == "forward")
    depth = sum(x for dr, x in instructions if dr == "down") - sum(
        x for dr, x in instructions if dr == "up"
    )

    print(f"{hor=}, {depth=}, {hor * depth=}")

    return hor * depth


def test_get_end_pos():
    lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    assert get_end_pos(lines) == 150


if __name__ == "__main__":
    test_get_end_pos()
    main()
