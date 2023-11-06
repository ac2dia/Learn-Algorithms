from unittest import TestCase

from solution import Solution, ListNode


class TestSolution(TestCase):
    def test_add_two_numbers(self):
        # given
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

        expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))

        # when
        actual = Solution.addTwoNumbers(self, l1, l2)

        # then
        while expected is not None and actual is not None:
            self.assertEqual(expected.val, actual.val)

            expected = expected.next
            actual = actual.next

