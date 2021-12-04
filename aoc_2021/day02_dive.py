"""
Day 2: Dive!
https://adventofcode.com/2021/day/2

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day02_input.txt'


def part1(data):
    h_pos = 0
    depth = 0

    for instruction in data:
        direction, val = __parse_instruction(instruction)

        if direction == 'forward':
            h_pos += val
        elif direction == 'down':
            depth += val
        elif direction == 'up':
            depth -= val
        else:
            raise Exception("Invalid direction:", direction)

    return h_pos * depth


def part2(data):
    h_pos = 0
    depth = 0
    aim = 0

    for instruction in data:
        direction, val = __parse_instruction(instruction)

        if direction == 'forward':
            h_pos += val
            depth += aim * val
        elif direction == 'down':
            aim += val
        elif direction == 'up':
            aim -= val
        else:
            raise Exception("Invalid direction:", direction)

    return h_pos * depth


def __parse_instruction(ins):
    e = ins.split(' ')
    return e[0], int(e[1])


class TestDay02(unittest.TestCase):
    sample_test_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    def test_part1_sample_data(self):
        result = part1(self.sample_test_data)
        self.assertEqual(150, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(2073315, result)

    def test_part2_sample_data(self):
        result = part2(self.sample_test_data)
        self.assertEqual(900, result)

    def test_part2(self):
        data = read_input(input_file)

        result = part2(data)
        self.assertEqual(1840311528, result)


if __name__ == '__main__':
    unittest.main()
