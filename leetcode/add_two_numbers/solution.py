from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_values = []
        l2_values = []

        while l1 is not None:
            l1_values.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            l2_values.append(l2.val)
            l2 = l2.next

        l1_values.reverse()
        l1_int = int(''.join(map(str, l1_values)))

        l2_values.reverse()
        l2_int = int(''.join(map(str, l2_values)))

        l3_values = list(map(int, str(l1_int + l2_int)))
        l3_values.reverse()

        l3 = ListNode()
        current = l3
        for val in l3_values:
            current.next = ListNode(val)
            current = current.next

        return l3.next

