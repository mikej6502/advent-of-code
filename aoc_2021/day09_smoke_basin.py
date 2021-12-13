"""
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day09_input.txt'
test_input_file = r'resources/day09_test_input.txt'


def part1(data):
    lowest_nums = __find_lowest_points(data)

    total = 0
    for num in lowest_nums:
        total += num[0]

    return total + len(lowest_nums)


def __find_lowest_points(data):
    height = len(data)
    width = len(data[0])

    lowest_nums = []
    for row, line in enumerate(data):
        for col, num in enumerate(line):
            # check all four neighbours
            current = int(num)
            lowest = True
            for c in __get_neighbours(row, col, height, width):
                r = c[0]
                c = c[1]
                candidate = int(data[r][c])
                if current >= candidate:
                    lowest = False
            if lowest:
                lowest_nums.append((current, (row, col)))
    return lowest_nums


def __get_neighbours(row, col, height, width):
    n1 = (row - 1, col)
    n2 = (row + 1, col)
    n3 = (row, col + 1)
    n4 = (row, col - 1)

    candidates = [n1, n2, n3, n4]

    results = []

    for candidate in candidates:
        r = candidate[0]
        c = candidate[1]

        if 0 <= r < height and 0 <= c < width:
            results.append(candidate)

    return results


def __get_unique_neighbours(data, row, col, seen, height, width):
    n1 = (row - 1, col)
    n2 = (row + 1, col)
    n3 = (row, col + 1)
    n4 = (row, col - 1)

    candidates = [n1, n2, n3, n4]

    results = []

    for candidate in candidates:
        r = candidate[0]
        c = candidate[1]

        if (r, c) in seen:
            continue

        if 0 <= r < height and 0 <= c < width:
            num = int(data[r][c])
            if num != 9:
                results.append(candidate)

    return results


def part2(data):
    height = len(data)
    width = len(data[0])

    lowest_nums = __find_lowest_points(data)

    # find all the basins
    basin_totals = []

    for lowest_num in lowest_nums:
        seen = set()
        basin = []
        res = __calc_basin(data, lowest_num[0], lowest_num[1][0], lowest_num[1][1], seen, basin, height, width)
        basin_totals.append(len(res))

    basin_totals.sort()
    return basin_totals[-3] * basin_totals[-2] * basin_totals[-1]


def __calc_basin(data, num, r, c, seen, basin, height, width):
    # Add the current number
    if (r, c) not in seen:
        basin.append(num)
        seen.add((r, c))

    neighbours = __get_unique_neighbours(data, r, c, seen, height, width)
    for c in neighbours:
        row = c[0]
        col = c[1]

        candidate = int(data[row][col])
        if candidate != 9:
            if (row, col) not in seen:
                basin.append(candidate)
            seen.add((row, col))
        __calc_basin(data, candidate, row, col, seen, basin, height, width)

    return basin


class TestDay09(unittest.TestCase):
    def test_part1_sample_data(self):
        data = read_input(test_input_file)
        result = part1(data)
        self.assertEqual(15, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(504, result)

    def test_part2_sample_data(self):
        data = read_input(test_input_file)
        result = part2(data)
        self.assertEqual(1134, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(1558722, result)


if __name__ == '__main__':
    unittest.main()
