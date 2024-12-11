"""
advent of code 2024 day 10
https://adventofcode.com/2024/day/10
"""


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
START = 0
GOAL = 9

# FOUND = set()


def apply_dir(pos, d):
    return pos[0] + d[0], pos[1] + d[1]


def move(curr, unique_found, found, topographic_map, h, w):
    if topographic_map[curr[0]][curr[1]] == GOAL:
        unique_found.add(curr)
        found.append(curr)
        return

    for direction in DIRECTIONS:
        nxt = apply_dir(curr, direction)
        if nxt[0] < 0 or nxt[0] >= h or nxt[1] < 0 or nxt[1] >= w:
            continue
        if topographic_map[curr[0]][curr[1]] + 1 != topographic_map[nxt[0]][nxt[1]]:
            continue
        move(nxt, unique_found, found, topographic_map, h, w)


def count_trails(topographic_map, trailheads, h, w):
    unique = 0
    total = 0

    for trailhead in trailheads:
        unique_found = set()
        found = []

        move(trailhead, unique_found, found, topographic_map, h, w)

        unique += len(unique_found)
        total += len(found)
    return unique, total


def main():
    data = open('inputs/day10.txt').read().strip().split('\n')
    h, w = len(data), len(data[0])

    topographic_map = []
    trailheads = set()

    for i in range(h):
        row = []
        for j in range(w):
            val = int(data[i][j])
            row.append(val)
            if val == START:
                trailheads.add((i, j))
        topographic_map.append(row)

    p1, p2 = count_trails(topographic_map, trailheads, h, w)
    print(p1, p2, sep='\n')


main()
