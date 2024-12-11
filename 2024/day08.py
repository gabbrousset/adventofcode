"""
advent of code 2024 day 8
https://adventofcode.com/2024/day/8
"""

def find_all(line, txt):
    idx = 0
    size = len(txt)
    indices = []
    while (idx := line.find(txt, idx)) != -1:
        indices.append(idx)
        idx += size
    return indices


def get_coords(idx, w):
    r = (idx // w) + 1
    c = (idx % w) + 1
    return r, c


def part1(data, h, w):
    anti_nodes = set()
    antennas = set(data)
    antennas.remove('.')

    for antenna in antennas:
        coords = find_all(data, antenna)
        for i in range(len(coords)):
            r_a, c_a = get_coords(coords[i], w)
            for j in range(i + 1, len(coords)):
                r_b, c_b = get_coords(coords[j], w)

                d_r = r_a - r_b
                d_c = c_a - c_b

                a = (r_a + d_r, c_a + d_c)
                b = (r_b - d_r, c_b - d_c)

                if 0 < a[0] <= h and 0 < a[1] <= w:
                    anti_nodes.add(a)
                if 0 < b[0] <= h and 0 < b[1] <= w:
                    anti_nodes.add(b)

    return len(anti_nodes)


def part2(data, h, w):
    anti_nodes = set()
    antennas = set(data)
    antennas.difference_update(['.', '#'])

    for antenna in antennas:
        coords = find_all(data, antenna)
        for i in range(len(coords)):
            r_a, c_a = get_coords(coords[i], w)
            for j in range(i + 1, len(coords)):
                r_b, c_b = get_coords(coords[j], w)

                d_r = r_a - r_b
                d_c = c_a - c_b

                a = [r_b + d_r, c_b + d_c]
                while 0 < a[0] <= h and 0 < a[1] <= w:
                    anti_nodes.add(tuple(a))
                    a[0] += d_r
                    a[1] += d_c

                b = [r_a - d_r, c_a - d_c]
                while 0 < b[0] <= h and 0 < b[1] <= w:
                    anti_nodes.add(tuple(b))
                    b[0] -= d_r
                    b[1] -= d_c

    return len(anti_nodes)


def main():
    data = open('inputs/day8.txt').read().strip().split('\n')
    h = len(data)
    w = len(data[0])
    data = ''.join(data)
    print(part1(data, h, w))
    print(part2(data, h, w))


main()
