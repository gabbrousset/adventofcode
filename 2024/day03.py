"""
advent of code 2024 day 3
https://adventofcode.com/2024/day/3
"""

DO = 'do()'
DONT = "don't()"


def mul_line(mul_c):
    mul_c = mul_c[:8]

    end = mul_c.find(')')

    if end == -1:
        return 0

    line = mul_c[:end]

    nums = line.split(',')
    if len(nums) != 2:
        return 0

    a, b = nums
    if not (a.isdigit() and b.isdigit()):
        return 0

    a, b = int(a), int(b)
    return a * b


def part1(data):
    res = 0
    for line in data:
        line = line.split('mul(')[1:]
        for mul_c in line:
            res += mul_line(mul_c)
    return res


def part2(data):
    res = 0

    flag = 0    # 0 = do, 1 = dont

    for line in data:
        line = line.split('mul(')
        for complete in line:
            mul_c = complete[:8]

            if flag == 0:
                res += mul_line(mul_c)

            while True:
                if flag == 0 and complete.find(DONT) != -1:
                    flag = 1
                    complete = complete[complete.find(DONT) + len(DONT):]
                elif flag == 1 and complete.find(DO) != -1:
                    flag = 0
                    complete = complete[complete.find(DO) + len(DO):]
                else:
                    break

    return res


def main():
    data = open('inputs/day3.txt').read().strip().split('\n')
    print(part1(data))
    print(part2(data))


main()
