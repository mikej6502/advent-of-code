"""
Day 11: Dumbo Octopus
https://adventofcode.com/2021/day/11

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day11_input.txt'
test_input_file = r'resources/day11_test_input.txt'


def part1(data):
    grid = __create_grid(data)

    flashes = 0
    for _ in range(100):
        flashes += __step(grid)

    return flashes


def __step(grid):
    width = len(grid[0])
    height = len(grid)

    flashed = set()

    # rule 1: increment all numbers by 1
    for r, row in enumerate(list(grid)):
        for c, col in enumerate(row):
            grid[r][c] += 1

    # rule 2: any over 9 flash, and cause neighbours to flash too
    flashes = 0
    for _ in range(10):
        for r, row in enumerate(list(grid)):
            for c, col in enumerate(row):
                if grid[r][c] > 9:
                    if (r, c) not in flashed:
                        flashes += 1
                        flashed.add((r, c))
                        grid[r][c] = 0

                    neighbours = __get_neighbours(r, c, width, height)

                    for coordinates in neighbours:
                        if (coordinates[0], coordinates[1]) not in flashed:
                            grid[coordinates[0]][coordinates[1]] += 1

    return flashes


def __step_until__in_sync(grid):
    width = len(grid[0])
    height = len(grid)

    flashed = set()

    # rule 1: increment all numbers by 1
    for r, row in enumerate(list(grid)):
        for c, col in enumerate(row):
            grid[r][c] += 1

    # rule 2: any over 9 flash, and cause neighbours to flash too
    flashes = 0
    for _ in range(200):
        for r, row in enumerate(list(grid)):
            for c, col in enumerate(row):
                if grid[r][c] > 9:
                    if (r, c) not in flashed:
                        flashes += 1
                        flashed.add((r, c))
                        grid[r][c] = 0

                    neighbours = __get_neighbours(r, c, width, height)
                    # print(neighbours)
                    for coordinates in neighbours:
                        if (coordinates[0], coordinates[1]) not in flashed:
                            grid[coordinates[0]][coordinates[1]] += 1

        if __is_all_zeros_grid(grid):
            return width * height

    return flashes


def __create_grid(data):
    grid = []

    for row in data:
        r = []
        for col in row:
            r.append(int(col))
        grid.append(r)
    return grid


def __is_all_zeros_grid(grid):
    for row in grid:
        for c in row:
            if c != 0:
                return False
    return True


def __get_neighbours(row, col, width, height):
    # up and down
    n1 = (row - 1, col)
    n2 = (row + 1, col)
    n3 = (row, col + 1)
    n4 = (row, col - 1)

    # diagonals
    n5 = (row - 1, col - 1)
    n6 = (row + 1, col - 1)
    n7 = (row - 1, col + 1)
    n8 = (row + 1, col + 1)

    candidates = [n1, n2, n3, n4, n5, n6, n7, n8]

    results = []

    for candidate in candidates:
        r = candidate[0]
        c = candidate[1]

        if 0 <= r < height and 0 <= c < width:
            results.append(candidate)

    return results


def part2(data):
    total_squares = len(data) * len(data[0])

    grid = __create_grid(data)
    for step_no in range(2000):
        flashes = __step_until__in_sync(grid)
        if flashes == total_squares:
            break

    return step_no + 1


class TestDay11(unittest.TestCase):
    def test_part1_sample_data(self):
        data = read_input(test_input_file)
        result = part1(data)
        self.assertEqual(1656, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(1642, result)

    def test_part2_sample_data(self):
        data = read_input(test_input_file)
        result = part2(data)
        self.assertEqual(195, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(320, result)


if __name__ == '__main__':
    unittest.main()
