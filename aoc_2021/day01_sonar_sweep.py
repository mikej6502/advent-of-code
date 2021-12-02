"""
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest

input_file = r'resources/day01_input.txt'


def day01_part1(data):
    """
    How many measurements are larger than the previous measurement?
    :param data: list of measurements
    :return: count
    """
    count = 0
    prev = -1

    for i in range(1, len(data)):
        current = int(data[i])
        if current > prev:
            count += 1
        prev = current

    return count


def day01_part2(data):
    """
    Count the number of times the sum of measurements in this sliding window increases from the previous sum.
    Start by comparing the first and second three-measurement windows.
    :param data: list of measurements
    :return: count
    """
    count = 0
    prev_measurement_window = int(data[0]) + int(data[1]) + int(data[2])

    for i in range(1, (len(data) - 2)):
        measurement_window = int(data[i]) + int(data[i + 1]) + int(data[i + 2])

        if measurement_window > prev_measurement_window:
            count += 1
        prev_measurement_window = measurement_window

    return count


def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data


class TestDay01(unittest.TestCase):
    sample_test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_day1_test_data(self):
        result = day01_part1(self.sample_test_data)
        self.assertEqual(7, result)

    def test_day1_part1(self):
        data = read_input(input_file)

        result = day01_part1(data)
        self.assertEqual(1184, result)

    def test_day2_test_data(self):
        result = day01_part2(self.sample_test_data)
        self.assertEqual(5, result)

    def test_day1_part2(self):
        data = read_input(input_file)

        result = day01_part2(data)
        self.assertEqual(1158, result)


if __name__ == '__main__':
    unittest.main()
