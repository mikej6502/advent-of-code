"""
Day 12: Passage Pathing
https://adventofcode.com/2021/day/12

Note: This is a competitive programming exercise.
Implemented for speed in terms of solving the solution in as short a time as possible.
"""

import unittest
from collections import defaultdict
from shared.file_reader import read_input


input_file = r'resources/day12_input.txt'
test_input_file = r'resources/day12_test_input.txt'


def part1(data):
    """
    A graph problem, so need a variation of Depth First Search. We want all unique paths, not just one path
    """
    graph = defaultdict(list)

    for line in data:
        e = line.split('-')
        if e[1] != 'start':
            graph[e[0]].append(e[1])
        if e[0] != 'start':
            graph[e[1]].append(e[0])

    return find_unique_paths(graph, 'start', 'end')


def part2(data):
    """
    A graph problem, so need a variation of Depth First Search. We want all unique paths, not just one path
    """
    graph = defaultdict(list)

    for line in data:
        n1, n2 = line.rstrip().split('-')
        if n2 != 'start':
            graph[n1].append(n2)
        if n1 != 'start':
            graph[n2].append(n1)

    return find_unique_paths_part2(graph, 'start', 'end')


def find_unique_paths(graph, start, end):
    stack = [(start, {start})]
    total = 0

    while stack:
        node, visited = stack.pop()

        if node == end:
            total += 1
        else:
            for loc in graph[node]:
                # ignore the locations which are lowercase and have already been visited once
                # can visit the small caves once only (lowercase letters)
                if loc not in visited or loc.isupper():
                    stack.append((loc, visited | {loc}))
    return total


def find_unique_paths_part2(graph, start, end):
    stack = [(start, {start}, False)]
    total = 0

    # can visit the small caves twice only (lowercase letters)
    while stack:
        node, visited, visited_twice = stack.pop()

        if node == end:
            total += 1
        else:
            for loc in graph[node]:
                if loc not in visited or loc.isupper():
                    stack.append((loc, visited | {loc}, visited_twice))
                else:
                    if not visited_twice:
                        stack.append((loc, visited, True))
    return total


class TestDay12(unittest.TestCase):

    def test_part1_sample_data(self):
        data = read_input(test_input_file)
        result = part1(data)
        self.assertEqual(10, result)

    def test_part1(self):
        data = read_input(input_file)
        result = part1(data)
        self.assertEqual(5920, result)

    def test_part2_sample_data(self):
        data = read_input(test_input_file)
        result = part2(data)
        self.assertEqual(36, result)

    def test_part2(self):
        data = read_input(input_file)
        result = part2(data)
        self.assertEqual(155477, result)


if __name__ == '__main__':
    unittest.main()
