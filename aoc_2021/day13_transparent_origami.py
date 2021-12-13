"""
Day 13: Transparent Origami
https://adventofcode.com/2021/day/13

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day13_input.txt'
test_input_file = r'resources/day13_test_input.txt'


def part1(data):
    coordinates, instructions, size = __parse_data(data)

    new_coordinates = list(coordinates)

    for axis, fold_index in instructions[:1]:
        if axis == 'y':
            new_coordinates = fold_up(new_coordinates, fold_index)
        if axis == 'x':
            new_coordinates = fold_left(new_coordinates, fold_index)

    grid = __plot_grid(new_coordinates, size)
    return __count_hashes(grid)


def part2(data):
    coordinates, instructions, size = __parse_data(data)
    new_coordinates = list(coordinates)

    for axis, fold_index in instructions:
        if axis == 'y':
            new_coordinates = fold_up(new_coordinates, fold_index)
        if axis == 'x':
            new_coordinates = fold_left(new_coordinates, fold_index)

    grid = __plot_grid(new_coordinates, size)

    # Read the characters from the printed grid
    __print_grid(grid, (6, 40))
    return None


def fold_left(coordinates, x_fold):
    # fold left to right (vertical fold)
    new_coordinates = set()
    for x, y in coordinates:
        if x < x_fold:
            new_coordinates.add((x, y))
        if x > x_fold:
            # transpose
            new_x = x_fold * 2 - x
            new_y = y
            new_coordinates.add((new_x, new_y))
    return new_coordinates


def fold_up(coordinates, y_fold):
    new_coordinates = set()
    # fold up (horizontal)
    for x, y in coordinates:
        if y < y_fold:
            new_coordinates.add((x, y))
        if y > y_fold:
            # transpose
            new_x = x
            new_y = y_fold * 2 - y
            new_coordinates.add((new_x, new_y))
    return new_coordinates


def __plot_grid(coordinates, size):
    height, width = size
    grid = []

    for row in range(height):
        r = []
        for col in range(width):
            r.append(' ')
        grid.append(r)

    for coordinate in coordinates:
        x, y = coordinate
        grid[y][x] = '#'

    return grid


def __count_hashes(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == '#':
                count += 1
    return count


def __print_grid(grid, size):
    for row in grid[:size[0]]:
        for col in row[:size[1]]:
            print(col, end='')
        print('')
    print("\n\n")


def __parse_data(data):
    height = 0
    width = 0

    coordinates = []
    instructions = []

    for line in data:
        if 'fold' in line:
            e = line.split(' ')
            ins = e[2].split('=')
            instructions.append((ins[0], int(ins[1])))
        else:
            if len(line) == 0:
                continue
            x, y = map(int, line.split(','))

            width = max(width, x)
            height = max(height, y)
            coordinates.append((x, y))

    width += 1
    height += 1
    return coordinates, instructions, (height, width)


class TestDay13(unittest.TestCase):
    def test_part1_sample_data(self):
        data = read_input(test_input_file)
        result = part1(data)
        self.assertEqual(17, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(770, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        # self.assertEqual('EPUELPBR', result)


if __name__ == '__main__':
    unittest.main()
