from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def add(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Elementary MAth
        T: O(M + N)
        S: O(1) ans -> O(max(m,n))
        :param l1:
        :param l2:
        :return:
        """
        dummy_head = ListNode(-1)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total_sum = v1 + v2 + carry
            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next


