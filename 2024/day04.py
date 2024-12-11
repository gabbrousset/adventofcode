"""
advent of code 2024 day 4
https://adventofcode.com/2024/day/4
"""


def rotate_matrix(matrix):
    n_r, n_c = len(matrix), len(matrix[0])
    rotated_matrix = [[None] * n_r for _ in range(n_c)]

    for i in range(n_r):
        for j in range(n_c):
            rotated_matrix[j][i] = matrix[-i - 1][j]

    return rotated_matrix


def is_S_diag(matrix, S, r, c):
    for i in range(len(S)):
        if matrix[r + i][c + i] != S[i]:
            return 0
    return 1


def count_XMAS_rtl(matrix):
    xmas = 'XMAS'
    count = 0

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for r in range(n_rows):
        count += ''.join(matrix[r]).count(xmas)
        if r < n_rows - len(xmas) + 1:
            for c in range(0, n_cols - len(xmas) + 1):
                count += is_S_diag(matrix, xmas, r, c)

    return count


def part1(matrix):
    count = 0
    for _ in range(4):
        count += count_XMAS_rtl(matrix)
        matrix = rotate_matrix(matrix)
    return count


def count_MAS_crosses(matrix):
    mas = 'MAS'
    sam = 'SAM'
    count = 0

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for r in range(n_rows):
        if r < n_rows - len(mas) + 1:
            for c in range(0, n_cols - len(mas) + 1):
                if is_S_diag(matrix, mas, r, c) or is_S_diag(matrix, sam, r, c):
                    matrix_2 = rotate_matrix(matrix)
                    if is_S_diag(matrix_2, mas, c, -r - len(mas)) or is_S_diag(matrix_2, sam, c, -r - len(mas)):
                        count += 1
    return count


def part2(matrix):
    return count_MAS_crosses(matrix)


def main():
    data = open('inputs/day4.txt').read().strip().split('\n')
    data = list(map(list, data))
    print(part1(data))
    print(part2(data))


main()
