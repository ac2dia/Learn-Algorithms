from unittest import TestCase

import solution


class TestSolution(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_solution(self):
        self.assertEqual(solution.solution(8, 4, [2, 3, 6]), 2)
        self.assertEqual(solution.solution(5, 4, [1, 3]), 1)
        self.assertEqual(solution.solution(4, 1, [1, 2, 3, 4]), 4)
