from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param head:
        :param k:
        :return:
        I/P : 1 -> 2 -> 3 -> 4 -> 5, k = 2
        o/p:  4 -> 5 -> 1 -> 2 -> 3

        """

        # base cases
        if not head or head.next:
            return head

        oldTail = head
        size = 1
        while oldTail.next:
            oldTail = oldTail.next
            size += 1

        # build the ring
        oldTail.next = head

        newTail = head

        # find the new tail
        for _ in range(size - k % size - 1):
            newTail = newTail.next
        # new Head -> k % size
        newHead = newTail.next

        # break the ring
        newTail.next = None
        return newHead
