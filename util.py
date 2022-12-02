def read_day(n):
    with open(f'./data/day{n}.txt', 'r') as file:
        return file.read()


def run_parts(day, part1, part2=None):
    data = read_day(day)
    print("Part 1:", part1(data))
    if part2 != None:
        print("Part 2:", part2(data))
