from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def swap_nodes_in_pairs_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        pointer = head
        pre_head = ListNode(-1)
        prev = pre_head

        while pointer and pointer.next:
            first = pointer
            second = pointer.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            pointer = first.next
        return pre_head.next

    def swap_nodes_in_pairs_v0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swap_nodes_in_pairs_v1(second.next)
        second.next = first

        return second
