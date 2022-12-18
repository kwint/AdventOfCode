import re


def test():
    data = open("input_test", "r").read().splitlines()

    result = main(data)
    print(f"test result: {result}")
    result == 0


def prod():
    data = open("input", "r").read().splitlines()

    result = main(data)
    print(f"prod result: {result}")

def get_columns(data) -> list[list[str]]:
    num_cols = int(data[-1][-2])
    columns = [[] for i in range(num_cols)]
    for row in reversed(data[:-1]):
        for i in range(num_cols):
            crate = re.search(r'[A-Z]', row[4*i:4*(i+1)])
            if crate is not None:
                columns[i].append(crate.group(0))

    print(columns)
    return columns

def main(data: list):

    split_line = data.index("")
    columns = get_columns(data[:split_line])

    for instruction in data[split_line+1:]:
        _, amount, _, src, _, to = instruction.split(" ")
        for _ in range(int(amount)):
            columns[int(to)-1].append(columns[int(src)-1].pop(-1))

    res = [column[-1] for column in columns]
    return "".join(res)
    


if __name__ == "__main__":
    test()
    prod()
