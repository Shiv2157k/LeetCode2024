from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def partition_list(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param head:
        :param x:
        :return:
        """

        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next
