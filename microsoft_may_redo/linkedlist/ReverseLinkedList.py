from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        rev_head = None
        pointer = head

        while pointer:
            next_node = pointer
            pointer.next = rev_head
            rev_head = pointer
            pointer = next_node
        return rev_head

    def reverse_v0(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        node = self.reverse_v0(head.next)
        head.next.next = head
        head.next = None
        return node
