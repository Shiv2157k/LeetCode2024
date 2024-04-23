from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head:
            return head

        prev = None
        pointer = head
        while pointer:
            nextNode = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nextNode
        return prev
