from unittest import TestCase

import solution


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution(["O.X", ".O.", "..X"]), 1)
        self.assertEqual(solution.solution(["OOO", "...", "XXX"]), 0)
        self.assertEqual(solution.solution(["...", ".X.", "..."]), 0)
        self.assertEqual(solution.solution(["...", "...", "..."]), 1)
