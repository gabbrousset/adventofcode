"""
advent of code 2024 day 11
https://adventofcode.com/2024/day/11
"""


def part1(stones):
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue
            string_stone = str(stone)
            digits_stone = len(string_stone)
            if digits_stone % 2 == 0:
                new_stones += [int(string_stone[:digits_stone // 2]), int(string_stone[digits_stone // 2:])]
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


dp = {}


# returns num of stones created by single stone after n blinks
def blink(stone, blinks, max_blinks):
    if blinks == 0:
        return 1

    if stone not in dp:
        dp[stone] = [0] * (max_blinks + 1)

    if dp[stone][blinks] != 0:
        return dp[stone][blinks]

    if stone == 0:
        dp[stone][blinks] = blink(1, blinks - 1, max_blinks)
        return dp[stone][blinks]

    string_stone = str(stone)
    digits_stone = len(string_stone)

    if digits_stone % 2:
        dp[stone][blinks] = blink(stone * 2024, blinks - 1, max_blinks)
        return dp[stone][blinks]

    a, b = [int(string_stone[:digits_stone // 2]), int(string_stone[digits_stone // 2:])]
    dp[stone][blinks] = blink(a, blinks - 1, max_blinks) + blink(b, blinks - 1, max_blinks)
    return dp[stone][blinks]


def part2(stones):
    blinks = 75

    count = 0
    for stone in stones:
        count += blink(stone, blinks, blinks)

    return count


def main():
    data = open('inputs/day11.txt').read().strip()
    stones = list(map(int, data.split(' ')))
    print(part1(stones))
    print(part2(stones))


main()
