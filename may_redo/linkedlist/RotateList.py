from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def rotate_list(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach:
        :param head:
        :param k:
        :return:
        """

        if not head or not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        # built circle
        old_tail.next = head

        # traverse
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
