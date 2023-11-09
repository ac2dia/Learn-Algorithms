from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_longest_palindrome(self):
        palindrome_list = [
            Solution().longestPalindrome("babad"),
            Solution().longestPalindrome("cbbd"),
            Solution().longestPalindrome("a"),
            Solution().longestPalindrome("ac"),
            Solution().longestPalindrome("bb"),
        ]

        for palindrome in palindrome_list:
            self.assertIn(palindrome, ["bab", "bb", "a", "c", "bb"])

