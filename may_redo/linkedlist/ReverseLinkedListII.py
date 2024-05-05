from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Approach: Reverse
        T: O(N)
        S: O(N)
        :param head:
        :param left:
        :param right:
        :return:
        """

        pre_head = ListNode(-1, head)
        left_tail = pre_head
        # traverse until the left tail that is node before left
        for _ in range(1, left):
            left_tail = left_tail.next

        # after the traverse this will be the reverse Head
        rev_head = left_tail
        right_head = left_tail.next

        # we reach until the node where right is pointed at the same time we reverse -> revHead
        # as well as the nodes after the right pointer -> rightHead
        for _ in range(left, right + 1):
            next_node = right_head.next
            right_head.next = rev_head
            rev_head = right_head
            right_head = next_node
        #                     l              r
        # left_tail = 2 <-> 3 <- 4 <- 5 <- 6 -> 7
        # link the tail of the reverse node with the right head
        left_tail.next.next = right_head
        # link the tail of left with the reverse node head
        left_tail.next = rev_head
        return pre_head.next
