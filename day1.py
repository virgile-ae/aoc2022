from util import run_parts


def part1(data):
    sums = [eval(x.replace('\n', '+')) for x in data.split('\n\n')]
    return max(sums)


def part2(data):
    sums = [eval(x.replace('\n', '+')) for x in data.split('\n\n')]
    return sum(sorted(sums, reverse=True)[:3])


run_parts(1, part1, part2)
