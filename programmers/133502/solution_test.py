import unittest

import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution([2, 1, 1, 2, 3, 1, 2, 3, 1]), 2)
        self.assertEqual(solution.solution([1, 3, 2, 1, 2, 1, 3, 1, 2]), 0)
        self.assertEqual(solution.solution([1, 2, 3, 1, 1, 2, 3, 1]), 2)
        self.assertEqual(solution.solution([1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1]), 3)


if __name__ == '__main__':
    unittest.main()
