from unittest import TestCase

from solution import Solution


class TestSolution(TestCase):
    def test_convert(self):
        # when
        s = "PAYPALISHIRING"
        numRows = 3

        # then
        output = Solution.convert(self, s, numRows)

        # assert
        self.assertEqual(output, "PAHNAPLSIIGYIR")

