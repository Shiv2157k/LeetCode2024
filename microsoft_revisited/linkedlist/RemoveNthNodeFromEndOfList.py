from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def removeNthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        preHead = ListNode(-1)
        preHead.next = head
        first = preHead
        second = preHead

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return preHead.next
