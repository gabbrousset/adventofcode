"""
advent of code 2024 day 2
https://adventofcode.com/2024/day/2
"""


def checkReport(line):
    if line[0] < line[1]:
        for idx in range(len(line) - 1):
            if not 1 <= line[idx + 1] - line[idx] <= 3:
                return False
    else:
        for idx in range(len(line) - 1):
            if not 1 <= line[idx] - line[idx + 1] <= 3:
                return False

    return True


def part1(data):
    return sum([checkReport(line) for line in data])


def part2(data):
    count = 0
    for line in data:
        if checkReport(line):
            count += 1
        else:
            for i in range(len(line)):
                l = line[:]
                l.pop(i)
                if checkReport(l):
                    count += 1
                    break
    return count


def main():
    data = open('inputs/day2.txt').read().strip().split('\n')
    data = [list(map(int, report.strip().split())) for report in data]
    print(part1(data))
    print(part2(data))


main()
