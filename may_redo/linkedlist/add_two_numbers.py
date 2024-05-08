from typing import Optional


class ListNode:


    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: School Book Addition
        T: O(max(m, n))
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """

        pre_head = ListNode(-1)
        prev = pre_head
        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10
            prev.next = ListNode(curr_sum % 10)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return pre_head.next