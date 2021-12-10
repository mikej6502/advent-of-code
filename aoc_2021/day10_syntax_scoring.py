"""
Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day10_input.txt'
input_test_file = r'resources/day10_test_input.txt'

brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

scoring_part1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scoring_part2 = {')': 1, ']': 2, '}': 3, '>': 4}


def part1(data):
    score = 0
    for line in data:
        res = __is_corrupt(line)
        if res[0]:
            score += scoring_part1[res[1]]
    return score


def part2(data):
    total_score = 0
    all_scores = []

    for line in data:
        res = __is_corrupt(line)
        if not res[0]:
            to_complete = __complete_line(line)
            score = 0
            for c in to_complete:
                score = score * 5
                score += scoring_part2[c]
            all_scores.append(score)
            total_score += score

    all_scores.sort()
    return all_scores[int(len(all_scores) / 2)]


def __is_corrupt(line):
    stack = []

    for c in line:
        if c in brackets.keys():
            stack.append(c)
        else:
            if not __is_closing_character(stack.pop(), c):
                return True, c
    return False, ''


def __complete_line(line):
    stack = []

    for c in line:
        if c in brackets.keys():
            stack.append(c)
        else:
            if not __is_closing_character(stack.pop(), c):
                return []

    required = []
    stack.reverse()
    for c in stack:
        required.append(__get_closing_character(c))

    return required


def __is_closing_character(opening_char, closing_char):
    return brackets[opening_char] == closing_char


def __get_closing_character(opening_char):
    return brackets[opening_char]


class TestDay10(unittest.TestCase):
    def test_part1_sample_data(self):
        data = read_input(input_test_file)
        result = part1(data)
        self.assertEqual(26397, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(216297, result)

    def test_part2_sample_data(self):
        data = read_input(input_test_file)
        result = part2(data)
        self.assertEqual(288957, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(2165057169, result)


if __name__ == '__main__':
    unittest.main()
