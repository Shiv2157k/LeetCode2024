from typing import Optional



class ListNode:


    def __init__(self, val: int=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        """
        Approach: SchoolBook Addition
        T: O(N)
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """
        # validation:
        if not l1 or not l2:
            return l1 or l2

        carry = 0
        preHead = ListNode(-1)
        prev = preHead

        while l1 or l1 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            currSum = val1 + val2 + carry
            carry = carry // 10

            prev.next = ListNode(currSum % 10)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return preHead.next