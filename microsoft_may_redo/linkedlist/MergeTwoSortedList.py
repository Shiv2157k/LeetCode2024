from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param l1:
        :param l2:
        :return:
        """

        pre_head = ListNode(-1)
        prev = pre_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 or l2
        return pre_head.next

    def merge_two_sorted_lists_v0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param l1:
        :param l2:
        :return:
        """

        if not l1:
            return l1
        elif not l2:
            return l2
        elif l1.val <= l2.val:
            l1.next = self.merge_two_sorted_lists_v0(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_sorted_lists_v0(l1, l2.next)
            return l2
