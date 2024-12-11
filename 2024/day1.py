"""
advent of code 2024 day 1
https://adventofcode.com/2024/day/1
"""


def part1(left, right):
    diff = 0
    for a, b in zip(left, right):
        diff += abs(a - b)

    return diff


def part2(left, right):
    res = 0
    for num in left:
        res += num * right.count(num)

    return res


def main():
    data = open('inputs/day1.txt').read().strip().split('\n')
    left, right = [], []

    for line in data:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    print(part1(left, right))
    print(part2(left, right))


main()
