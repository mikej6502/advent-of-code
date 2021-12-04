"""
Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day03_input.txt'


def part1(data):
    bits_0, bits_1 = __sum_bits(data)

    gamma_binary_str = ''
    epsilon_binary_str = ''

    for i in range(len(data[0])):
        if bits_0[i] > bits_1[i]:
            gamma_binary_str += '0'
            epsilon_binary_str += '1'
        else:
            gamma_binary_str += '1'
            epsilon_binary_str += '0'

    return int(gamma_binary_str, 2) * int(epsilon_binary_str, 2)


def __sum_bits(data):
    bits_0 = {}
    bits_1 = {}

    for number in data:
        for i, bit in enumerate(number):
            bits_0.setdefault(i, 0)
            bits_1.setdefault(i, 0)

            if bit == '0':
                bits_0[i] += 1
            else:
                bits_1[i] += 1

    return bits_0, bits_1


def part2(data):
    o2_rating = __find_oxygen_generator_rating(list(data))
    co2_rating = __find_co2_scrub_rating(list(data))

    return int(o2_rating, 2) * int(co2_rating, 2)


def __get_most_common_bit(bits_0, bits_1, numbers):
    binary = ''
    for i in range(len(numbers[0])):
        if bits_0[i] > bits_1[i]:
            binary += '0'
        else:
            binary += '1'
    return binary


def __find_oxygen_generator_rating(data):
    return __find_rating(data, __get_common_bit, False)


def __find_co2_scrub_rating(data):
    return __find_rating(data, __get_common_bit, True)


def __find_rating(data, bit_calculation, least_common):
    for i in range(len(data[0])):
        temp_data = list(data)
        bit = bit_calculation(temp_data, i, least_common)

        for number in list(data):
            if number[i] != bit:
                data.remove(number)

            if len(data) == 1:
                return data[0]
    return None


def __get_common_bit(numbers, pos, least_common=False):
    zeros = 0
    ones = 0

    for number in numbers:
        if number[pos] == '0':
            zeros += 1
        if number[pos] == '1':
            ones += 1

    if least_common:
        if zeros == ones or ones > zeros:
            return '1'
    else:
        if zeros != ones and ones < zeros:
            return '1'

    return '0'


class TestDay03(unittest.TestCase):
    sample_test_data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001',
                        '00010', '01010']

    def test_part1_sample_data(self):
        result = part1(self.sample_test_data)
        self.assertEqual(198, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(3895776, result)

    def test_part2_sample_data(self):
        result = part2(self.sample_test_data)
        self.assertEqual(230, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(7928162, result)


if __name__ == '__main__':
    unittest.main()
