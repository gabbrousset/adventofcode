"""
advent of code 2024 day 6
https://adventofcode.com/2024/day/6
"""
import copy


UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

EMPTY = '.'
OBSTACLE = '#'


def is_guard_leaving(guard, d, h, w):
    guard_r, guard_c = guard
    if d == UP and guard_r == 0:
        return True
    if d == DOWN and guard_r == h - 1:
        return True
    if d == LEFT and guard_c == 0:
        return True
    if d == RIGHT and guard_c == w - 1:
        return True
    return False


def moveGuard(obstacle_map, guard, d):
    guard_r, guard_c = guard
    if d == UP:
        if obstacle_map[guard_r - 1][guard_c] != OBSTACLE:
            return (guard_r - 1, guard_c), d
        return guard, RIGHT
    if d == DOWN:
        if obstacle_map[guard_r + 1][guard_c] != OBSTACLE:
            return (guard_r + 1, guard_c), d
        return guard, LEFT
    if d == LEFT:
        if obstacle_map[guard_r][guard_c - 1] != OBSTACLE:
            return (guard_r, guard_c - 1), d
        return guard, UP
    if d == RIGHT:
        if obstacle_map[guard_r][guard_c + 1] != OBSTACLE:
            return (guard_r, guard_c + 1), d
        return guard, DOWN


def simulateGuardLeaving(obstacle_map, guard, d, h, w):
    unique_positions = {guard}

    while not is_guard_leaving(guard, d, h, w):
        guard, d = moveGuard(obstacle_map, guard, d)

        if d in obstacle_map[guard[0]][guard[1]]:
            return unique_positions, False

        obstacle_map[guard[0]][guard[1]].append(d)
        unique_positions.add(guard)

    return unique_positions, True


def part1(obstacle_map_og, guard, d, h, w):
    obstacle_map = copy.deepcopy(obstacle_map_og)
    return len(simulateGuardLeaving(obstacle_map, guard, d, h, w)[0])


def part2(obstacle_map_og, guard, d, h, w):
    obstacle_map = copy.deepcopy(obstacle_map_og)

    unique_positions, leaving = simulateGuardLeaving(obstacle_map, guard, d, h, w)
    unique_positions.remove(guard)

    count = 0

    for candidate in unique_positions:
        obstacle_map = copy.deepcopy(obstacle_map_og)
        obstacle_map[candidate[0]][candidate[1]] = OBSTACLE

        unique_positions, leaving = simulateGuardLeaving(obstacle_map, guard, d, h, w)
        if not leaving:
            count += 1

    return count


def main():
    data = open('inputs/day6.txt').read().strip().split('\n')
    h, w = len(data), len(data[0])
    data = [list(row) for row in data]

    obstacle_map = []
    guard = None
    d = None

    for i, line in enumerate(data):
        row = []
        for j, val in enumerate(line):
            if val == OBSTACLE:
                row.append(val)
            else:
                row.append([])
                if val in DIRECTIONS:
                    d = val
                    guard = (i, j)
                    row[-1].append(d)
        obstacle_map.append(row)

    print(part1(obstacle_map, guard, d, h, w))
    print(part2(obstacle_map, guard, d, h, w))


main()
