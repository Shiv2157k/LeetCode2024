from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param head:
        :param x:
        :return:
        """

        before_head = ListNode(-1)
        after_head = ListNode(-1)
        before_ptr = before_head
        after_ptr = after_head

        while head:

            if head.val < x:
                before_ptr.next = head
                before_ptr = before_ptr.next
            else:
                after_ptr.next = head
                after_ptr = after_ptr.next
            head = head.next
        after_ptr.next = None
        before_ptr.next = after_head.next
        return before_head.next
