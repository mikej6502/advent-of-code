"""
Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day08_input.txt'
test_input_file = r'resources/day08_test_input.txt'


def part1(data):
    """
    Part one, count all the 7 segment displays showing a '1', '4', '7' or '8'
    Each of these has a unique number of 'on' segments, so very easy to identify them
    """
    entries = __parse_data(data)
    count = 0
    for entry in entries:
        for e in entry[1]:
            if len(e) == 2 or len(e) == 4 or len(e) == 3 or len(e) == 7:
                count += 1
    return count


def part2(data):
    """
    A little more tricky. Given only a list of segments that are 'on', but scrambled,
    correctly map the scrambled digits to the correct number to sum up the output
    As above, some digits are easy to identify, but several have the same number of segments, so let the detective
    work begin.

    Not particularly pretty or elegant,
    but the method below will at least sort the mixed up input to identify the correct digits
    """
    total = 0
    entries = __parse_data(data)

    for entry in entries:
        # two maps, as want to map from digit -> segments and segments -> digits for easy reference later
        digits = {}
        segments = {}

        # several passes for each set of signal patterns to identify them all correctly,
        # with effort maybe able to reduce this
        __decode_numbers_with_unique_no_of_segments(entry[0], digits, segments)

        __decode_three_and_nine(entry[0], digits, segments)

        __decode_zero_and_six(entry[0], digits, segments)

        __decode_two_and_five(entry[0], digits, segments)

        # wow! convoluted, but managed to map each digit, now simply decode and make a four-digit number

        temp = ''
        temp += str(segments["".join(sorted(entry[1][0]))])
        temp += str(segments["".join(sorted(entry[1][1]))])
        temp += str(segments["".join(sorted(entry[1][2]))])
        temp += str(segments["".join(sorted(entry[1][3]))])

        number = int(temp)
        total += number
    return total


def __parse_data(data):
    entries = []

    for entry in data:
        parts = entry.split('|')
        signal_patterns = parts[0].rstrip().split(' ')
        output_vales = parts[1].lstrip().split(' ')

        data_in = []
        for i in signal_patterns:
            data_in.append(i)

        entries.append([data_in, output_vales])

    return entries


def __decode_numbers_with_unique_no_of_segments(entry, digits, segments):
    # map all the digits that we can identify based on unique number of segments
    for e in entry:
        if len(e) == 2:
            digits[1] = "".join(sorted(e))
            segments["".join(sorted(e))] = 1
        if len(e) == 3:
            digits[7] = "".join(sorted(e))
            segments["".join(sorted(e))] = 7
        if len(e) == 4:
            digits[4] = "".join(sorted(e))
            segments["".join(sorted(e))] = 4
        if len(e) == 7:
            digits[8] = "".join(sorted(e))
            segments["".join(sorted(e))] = 8


def __decode_three_and_nine(entry, digits, segments):
    for e in entry:
        # 2, 3 & 5 all contains 5 segments
        # however a 3 can be identified as it must contain both segments of a '1' (identified earlier)
        if len(e) == 5:
            # 3 must contain both 1's segments
            if digits[1][0] in e and digits[1][1] in e:
                digits[3] = "".join(sorted(e))
                segments["".join(sorted(e))] = 3
        # 0, 6 & 9 all contains 6 segments
        # however a 9 can be identified as it must contain both segments of a '4' (identified earlier)
        elif len(e) == 6:
            # 9 must contain all 4's segments
            if digits[4][0] in e and digits[4][1] in e and digits[4][2] in e and digits[4][3] in e:
                digits[9] = "".join(sorted(e))
                segments["".join(sorted(e))] = 9


def __decode_zero_and_six(entry, digits, segments):
    for e in entry:
        if len(e) == 6:
            # 0, 6 & 9 all contains 6 segments
            # 6 or 0 won't contain all elements of a '4', so can eliminate '9'
            if digits[4][0] not in e or digits[4][1] not in e or digits[4][2] not in e or digits[4][3] not in e:
                # a 9 must contain all segments of a '1'
                if digits[1][0] in e and digits[1][1] in e:
                    digits[0] = "".join(sorted(e))
                    segments["".join(sorted(e))] = 0
                # By process of elimination, must be a 6
                else:
                    digits[6] = "".join(sorted(e))
                    segments["".join(sorted(e))] = 6


def __decode_two_and_five(entry, digits, segments):
    for e in entry:
        # 2,3,5 all have 5 segments
        if len(e) == 5:
            # using a 6, it's possible to find the character mapped to segment 'c'
            six = digits[6]
            c_seg = ''
            # find the missing 'c' segment from the 6
            for c in 'abcdefg':
                if c not in six:
                    c_seg = c
                    break

            # ignore 3 and focus on 2 and 5
            if digits[1][0] not in e or digits[1][1] not in e:
                # 2 contains the 'c' segment
                if c_seg in e:
                    digits[2] = "".join(sorted(e))
                    segments["".join(sorted(e))] = 2
                # 5 does not contains the 'c' segment
                else:
                    digits[5] = "".join(sorted(e))
                    segments["".join(sorted(e))] = 5


class TestDay08(unittest.TestCase):

    def test_part1_sample_data(self):
        data = read_input(test_input_file)
        result = part1(data)
        self.assertEqual(26, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(543, result)

    def test_part2_sample_data(self):
        data = read_input(test_input_file)
        result = part2(data)
        self.assertEqual(61229, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(994266, result)


if __name__ == '__main__':
    unittest.main()
