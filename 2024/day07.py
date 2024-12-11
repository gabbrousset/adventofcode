"""
advent of code 2024 day 7
https://adventofcode.com/2024/day/7
"""


def mult(x, y):
    return x * y


def add(x, y):
    return x + y


def concat(x, y):
    shift_by = len(str(y))
    return (10 ** shift_by) * x + y


def is_target_possible(target, curr, values, idx, operators):
    if idx == len(values):
        return curr == target

    if curr > target:
        return False

    for op in operators:
        new_curr = op(curr, values[idx])
        if is_target_possible(target, new_curr, values, idx + 1, operators):
            return True
    return False


def solve_eqs_with_ops(equations, operators):
    total = 0
    for eq in equations:
        target, values = eq
        if is_target_possible(target, values[0], values, 1, operators):
            total += target
    return total


def part1(equations):
    operators = (add, mult)
    return solve_eqs_with_ops(equations, operators)


def part2(equations):
    operators = (add, mult, concat)
    return solve_eqs_with_ops(equations, operators)


def main():
    data = open('inputs/day7.txt').read().strip().split('\n')
    equations = []
    for line in data:
        res, values = line.split(':')
        res = int(res.strip())
        values = tuple(map(lambda x: int(x.strip()), values.strip().split(' ')))
        equations.append((res, values))

    print(part1(equations))
    print(part2(equations))


main()
