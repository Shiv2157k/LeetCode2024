from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def swapNodesInPairsV0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapNodesInPairsV0(second.next)
        second.next = first

        return second
        
    def swapNodesInPairsV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        preHead = ListNode(-1)
        prev = preHead

        while head and head.next:

            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return preHead.next



