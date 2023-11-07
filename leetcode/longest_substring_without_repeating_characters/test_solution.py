from unittest import TestCase

from solution import Solution


class TestSolution(TestCase):
    def test_length_of_longest_substring(self):
        # given
        solution = Solution()
        test_cases = [
            "abcabcbb",
            "bbbbb",
            "pwwkew",
        ]
        expected_results = [
            3,
            1,
            3,
        ]

        # when
        for i, test_case in enumerate(test_cases):
            # then
            self.assertEqual(expected_results[i], solution.lengthOfLongestSubstring(test_case))

