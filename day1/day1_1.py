from itertools import pairwise


def main():
    with open("day1/input.txt") as fp:
        lines = fp.readlines()

    lines = [int(line) for line in lines]
    num_increased_readings = count_increased_readings(lines)

    print(f"{num_increased_readings=}")
    assert num_increased_readings == 1184


def count_increased_readings(readings):
    return sum(b > a for a, b in pairwise(readings))


def test_count_increased_readings():
    lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    assert count_increased_readings(lines) == 7


if __name__ == "__main__":
    test_count_increased_readings()
    main()
