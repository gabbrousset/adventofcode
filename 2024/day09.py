"""
advent of code 2024 day 9
https://adventofcode.com/2024/day/9
"""


EMPTY = '.'


def checksum(blocks):
    res = 0
    for i, v in enumerate(blocks):
        if v == EMPTY:
            continue
        res += v * i
    return res


def get_blocks(disk_map):
    blocks = []
    block_sizes = {}

    for i, v in enumerate(disk_map):
        if i % 2:
            blocks.extend([EMPTY] * v)
        else:
            blocks.extend([i // 2] * v)
            block_sizes[i//2] = v

    return blocks, block_sizes


def part1(disk_map):
    blocks = get_blocks(disk_map)[0]
    moved = 0

    for idx in range(len(blocks)):
        while blocks[idx] == EMPTY and moved < len(blocks) - idx:
            blocks[idx] = blocks[-moved - 1]
            blocks[-moved - 1] = EMPTY
            moved += 1

    return checksum(blocks)


def empty_size(blocks, j, size):
    for n in range(size):
        if blocks[j + n] != EMPTY:
            return False
    return True


def part2(disk_map):
    blocks, block_sizes = get_blocks(disk_map)

    for i in range(len(blocks) - 1, -1, -1):
        val = blocks[i]
        if val != EMPTY:
            size = block_sizes[val]
            for j in range(i):
                if empty_size(blocks, j, size):
                    for n in range(size):
                        blocks[j + n] = val
                        blocks[i - n] = EMPTY
                    break

    return checksum(blocks)


def main():
    data = open('inputs/day9.txt').read().strip()
    data = list(map(int, data))
    print(part1(data))
    print(part2(data))



main()
