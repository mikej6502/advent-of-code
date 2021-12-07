"""
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input
from bresenham import bresenham


input_file = r'resources/day05_input.txt'
sample_input_file = r'resources/day05_test_input.txt'

# Not ideal, as need to know the max size of the grid, but for this inout data 1000 x 1000 is fine.
width = 1000
height = 1000


def part1(data):
    coordinates = __parse_data(data)

    grid = []
    for _ in range(height):
        row = []
        for c in range(width):
            row.append(0)

        grid.append(row)

    count = 0

    for c in coordinates:
        x1 = c[0][0]
        y1 = c[0][1]
        x2 = c[1][0]
        y2 = c[1][1]

        if x1 == x2:
            points = list(bresenham(x1, y1, x1, y2))
        elif y1 == y2:
            points = list(bresenham(x1, y1, x2, y1))
        else:
            continue

        for p in points:
            row = grid[p[1]]
            val = row[p[0]]
            val += 1
            row[p[0]] = val
            if val == 2:
                count += 1

    return count


def part2(data):
    coordinates = __parse_data(data)

    grid = []
    for _ in range(height):
        row = []
        for c in range(width):
            row.append(0)

        grid.append(row)

    count = 0

    for c in coordinates:
        x1 = c[0][0]
        y1 = c[0][1]
        x2 = c[1][0]
        y2 = c[1][1]

        points = list(bresenham(x1, y1, x2, y2))

        for p in points:
            row = grid[p[1]]
            val = row[p[0]]
            val += 1
            row[p[0]] = val
            if val == 2:
                count += 1

    return count


def __parse_data(data):
    coordinates = []
    for line in data:
        e = line.split('->')
        e1 = e[0].split(',')
        x1 = int(e1[0])
        x2 = int(e1[1])

        e2 = e[1].split(',')
        y1 = int(e2[0])
        y2 = int(e2[1])

        coordinates.append(((x1, x2), (y1, y2)))
    return coordinates


class TestDay04(unittest.TestCase):
    def test_part1_sample_data(self):
        result = part1(read_input(sample_input_file))
        self.assertEqual(5, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(5698, result)

    def test_part2_sample_data(self):
        result = part2(read_input(sample_input_file))
        self.assertEqual(12, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(15463, result)


if __name__ == '__main__':
    unittest.main()
