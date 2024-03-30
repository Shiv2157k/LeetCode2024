from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        """
        Approach: Elementary MAth
        T: O(max(m, n))
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """

        preHead = ListNode(-1)
        prev = preHead

        carry = 0

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            addSum = val1 + val2 + carry
            carry = addSum // 2

            prev.next = ListNode(addSum % 10)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return preHead.next
