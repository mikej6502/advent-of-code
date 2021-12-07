"""
Day 6: Lanternfish
https://adventofcode.com/2021/day/6

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest

input_file = r'resources/day07_input.txt'


class SpawnManager:
    def __init__(self, timers):
        self.fish = []
        for t in timers:
            self.fish.append(Fish(int(t)))

    def update(self):
        for f in list(self.fish):
            f.timer -= 1

            if f.timer < 0:
                f.timer = 6
                self.fish.append(Fish(8))

    def __len__(self):
        return len(self.fish)


class Fish:
    def __init__(self, timer):
        self.timer = timer


def part1(data):
    """
    Brute Force Solution modelled using OO - Fine for samll datasets, but grows exponentially
    """
    timers = data.split(',')
    spawner = SpawnManager(timers)

    for _ in range(80):
        spawner.update()

    return len(spawner)


def part2(data):
    """
    Brute Force Solution wont work here as the data set is too large and grows exponentially over too many days
    The list grows with each cycle, so need a way to stop that happening
    """

    timers = list(map(int, data.split(',')))

    # Dont store fish, but store a list of the number of fish at each state, as fish get state zero these can
    # be popped off the list, and a state 8 added
    # Here the list doesn't grow, so space complexity is O(1), meaning a very quick execution time
    # After all the cycles, simply add up the number of fish at each state to get the answer
    state = [0] * 9
    for fish_to_breed in timers:
        state[fish_to_breed] += 1

    for day in range(256):
        # remove all fish with zero timer
        breeding = state.pop(0)
        # add all fish with timer reset
        state[-2] += breeding
        # add back to the list
        state.append(breeding)

    return sum(state)


class TestDay06(unittest.TestCase):
    sample_test_data = '3, 4, 3, 1, 2'
    input_data = '1,3,1,5,5,1,1,1,5,1,1,1,3,1,1,4,3,1,1,2,2,4,2,1,3,3,2,4,4,4,1,3,1,1,4,3,1,5,5,1,1,3,4,2,1,5,3,4,5,5,2,5,5,1,5,5,2,1,5,1,1,2,1,1,1,4,4,1,3,3,1,5,4,4,3,4,3,3,1,1,3,4,1,5,5,2,5,2,2,4,1,2,5,2,1,2,5,4,1,1,1,1,1,4,1,1,3,1,5,2,5,1,3,1,5,3,3,2,2,1,5,1,1,1,2,1,1,2,1,1,2,1,5,3,5,2,5,2,2,2,1,1,1,5,5,2,2,1,1,3,4,1,1,3,1,3,5,1,4,1,4,1,3,1,4,1,1,1,1,2,1,4,5,4,5,5,2,1,3,1,4,2,5,1,1,3,5,2,1,2,2,5,1,2,2,4,5,2,1,1,1,1,2,2,3,1,5,5,5,3,2,4,2,4,1,5,3,1,4,4,2,4,2,2,4,4,4,4,1,3,4,3,2,1,3,5,3,1,5,5,4,1,5,1,2,4,2,5,4,1,3,3,1,4,1,3,3,3,1,3,1,1,1,1,4,1,2,3,1,3,3,5,2,3,1,1,1,5,5,4,1,2,3,1,3,1,1,4,1,3,2,2,1,1,1,3,4,3,1,3'

    def test_part1_sample_data(self):
        result = part1(self.sample_test_data)
        self.assertEqual(5934, result)

    def test_part1(self):
        result = part1(self.input_data)
        self.assertEqual(360268, result)

    def test_part2_sample_data(self):
        result = part2(self.sample_test_data)
        self.assertEqual(26984457539, result)

    def test_part2(self):
        result = part2(self.input_data)
        self.assertEqual(1632146183902, result)


if __name__ == '__main__':
    unittest.main()
