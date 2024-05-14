from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_nth_node(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param head:
        :param n:
        :return:
        """
        if not head:
            return head

        pre_head = ListNode(-1, head)
        first = pre_head

        for _ in range(n):
            first = first.next

        second = pre_head

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next if second.next else None
        return pre_head.next
