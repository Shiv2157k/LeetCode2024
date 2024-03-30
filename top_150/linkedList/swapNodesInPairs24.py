from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedLists:

    def swapNodesInPairsV0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N) -> stack space utilized for recursion
        :param head:
        :return:
        """

        # base case
        # Cannot swap the pairs
        if not head or not head.next:
            return head

        firstNode = head
        secondNode = head.next

        firstNode.next = self.swapNodesInPairsV0(secondNode.next)
        secondNode.next = firstNode
        return secondNode

    def swapNodesInPairsV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        preHead = ListNode(-1)
        preHead.next = head

        prev = preHead

        while head and head.next:
            firstNode = head
            secondNode = head.next

            # swap
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            # re-initialize prev and head
            prev = firstNode
            head = firstNode.next
        return preHead.next
