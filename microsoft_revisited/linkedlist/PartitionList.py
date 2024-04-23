from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param head:
        :param x:
        :return:
        """

        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = afterHead.next
        return beforeHead.next
