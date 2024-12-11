"""
advent of code 2024 day 5
https://adventofcode.com/2024/day/5
"""


def is_valid_update(update, dependencies):
    for i, page in enumerate(update):
        if page in dependencies:
            for dep in dependencies[page]:
                if dep in update[i + 1:]:
                    return False
    return True


def fix_first_page(corrected, dependencies):
    for i, page in enumerate(corrected):
        if page in dependencies:
            for dep in dependencies[page]:
                if dep in corrected[i + 1:] and (d_i := corrected.index(dep, i + 1)) != -1:
                    corrected[i] = dep
                    corrected[d_i] = page
                    return corrected, True
    return corrected, False


def fix_update(update, dependencies):
    corrected = update[:]

    flag = True
    while flag:
        corrected, flag = fix_first_page(corrected, dependencies)

    return corrected


def main():
    rules, updates = open('inputs/day5.txt').read().strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in rules.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updates.split('\n')]

    dependencies = {}
    for x, y in rules:  # x must be printed before y
        if y not in dependencies:
            dependencies[y] = []
        dependencies[y].append(x)

    p1 = 0
    p2 = 0
    for update in updates:
        if is_valid_update(update, dependencies):
            p1 += update[len(update)//2]
        else:
            corrected = fix_update(update, dependencies)
            p2 += corrected[len(corrected)//2]

    print(p1, p2, sep='\n')


main()
