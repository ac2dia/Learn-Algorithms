from unittest import TestCase

from solution import Solution


class TestSolution(TestCase):
    def test_two_sum(self):
        first_match_indexes = Solution.twoSum(self, [2, 7, 11, 15], 9)
        self.assertEqual(first_match_indexes, [0, 1])

        second_match_indexes = Solution.twoSum(self, [3, 2, 4], 6)
        self.assertEqual(second_match_indexes, [1, 2])

