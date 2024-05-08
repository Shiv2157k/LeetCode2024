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
        S: O(N)
        :param head:
        :param n:
        :return:
        """

        if not head:
            return head

        pre_head = ListNode(-1, head)
        first_node = pre_head

        # for _ in range(n + 1):
        for _ in range(n):
            first_node = first_node.next

        second_node = pre_head
        # while first_node:
        while first_node.next:
            first_node = first_node.next
            second_node = second_node.next

        second_node.next = second_node.next.next if second_node.next else None

        return pre_head.next



