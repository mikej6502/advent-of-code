"""
Day 4: Giant Squid
https://adventofcode.com/2021/day/4

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from shared.file_reader import read_input


input_file = r'resources/day04_input.txt'
test_data_input_file = r'resources/day04_test_input.txt'


def part1(data):
    """
    Bingo! Input contains the bingo boards and list of numbers called. Find the board that has a winning line
    A brute force approach on this one. No issues as dataset is small enough to get a result.
    """
    boards = __create_boards(data)
    numbers = map(int, data[0].split(','))

    for number in numbers:
        for board in boards:
            if __update(number, board):
                return __calc_board_result(board, number)
    return -1


def part2(data):
    """
    Find the board that wins last!
    A brute force approach on this one. No issues as dataset is small enough to get a result.
    """
    boards = __create_boards(data)
    numbers = map(int, data[0].split(','))

    winners = []

    for number in numbers:
        for i, board in enumerate(boards):
            if i not in winners:
                if __update(number, board):
                    winners.append(i)
                    if len(winners) == len(boards):
                        return __calc_board_result(board, number)
    return -1


def __calc_board_result(board, winning_num):
    """
    Find the sum of all unmarked numbers on the board
    :param board: bingo board
    :param winning_num: winning number
    :return: sum of unmarked numbers * the winning number
    """
    unmarked = 0

    for line in board:
        for number in line:
            if number[1] != 'x':
                unmarked += int(number[0])

    return unmarked * winning_num


def __update(n, board):
    """
    Update the board by marking off the number n.
    Check if there is a winning line (vertical or horizontal).
    :param n: number
    :param board: board to check
    :return: True if a winning line, otherwise False
    """
    
    # TODO: Function way too big and messy!
    
    # Scan each board and look for the number to mark off
    row_len = len(board[0])

    done = False
    for line_no, line in enumerate(board):
        for col_no, number in enumerate(line):
            if number[0] == int(n):
                number[1] = 'x'
                done = True
                break
        if done:
            break

    # check if the line is a horizontal winner
    candidate_row = board[line_no]
    count = 0
    for number in candidate_row:
        if number[1] == 'x':
            count += 1

    if count == row_len:
        return True

    # check if the line is a vertical winner
    count = 0
    candidate_col = col_no

    for r in range(row_len):
        row = board[r]
        if row[candidate_col][1] == 'x':
            count += 1

    if count == row_len:
        return True

    return False


def __create_boards(data):
    boards = []
    board = []
    for input in data[2:]:

        if len(input) == 0:
            boards.append(board)
            board = []
            continue

        nums = input.split(' ')

        line = []
        for n in nums:
            if n != '':
                line.append([int(n), '0'])

        board.append(line)

    boards.append(board)
    return boards


class TestDay04(unittest.TestCase):

    def test_part1_sample_data(self):
        data = read_input(test_data_input_file)
        result = part1(data)
        self.assertEqual(4512, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(31424, result)

    def test_part2_sample_data(self):
        data = read_input(test_data_input_file)
        result = part2(data)
        self.assertEqual(1924, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(23042, result)


if __name__ == '__main__':
    unittest.main()
