from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def deleteNode(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Re-write
        T: O(N)
        S: O(1)
        :param node:
        :return:
        """

        node.val = node.next.val
        node.next = node.next.next