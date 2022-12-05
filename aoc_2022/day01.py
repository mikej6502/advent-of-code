"""
Day 1: Calorie Counting
https://adventofcode.com/2022/day/1

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""
import unittest
from shared.file_reader import read_input

input_file = r'resources/day01_input.txt'


def part1(data):
    max_cals = -1
    cals = 0

    for n in data:
        if n == '':
            max_cals = max(max_cals, cals)
            cals = 0
        else:
            cals += int(n)

    return max_cals


def part2(data):
    cals = 0
    totals = []

    for n in data:
        if n == '':
            totals.append(cals)
            cals = 0
        else:
            cals += int(n)

    totals.sort(reverse=True)
    return totals[0] + totals[1] + totals[2]


class TestDay01(unittest.TestCase):
    def test_part1(self):
        data = read_input(input_file)

        result = part1(data)
        self.assertEqual(72602, result)

    def test_part2(self):
        data = read_input(input_file)

        result = part2(data)
        self.assertEqual(207410, result)


if __name__ == '__main__':
    unittest.main()
