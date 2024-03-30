from typing import Optional


class ListNode:

    def __init__(self, val: int=-1, next=None):
        self.val = val
        self.next = next


class LinkedListNodes:

    def reverseNodesInKGroupV1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :param head:
        :param k:
        :return:
        """

        pointer = head
        newHead = None
        ktail = None

        while pointer:

            count = 0
            pointer = head

            while count < k and pointer:
                count += 1
                pointer = pointer.next
            if count == k:
                revHead = self._reverseKNodes(head, k)

                if not newHead:
                    newHead = revHead
                if ktail:
                    ktail.next = revHead
                ktail = head
                head = pointer

        if ktail:
            ktail.next = head
        return newHead if not None else head

    def reverseNodesInKGroupV0(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        pointer = head
        count = 0

        while count < k and pointer:
            pointer = pointer.next
            count += 1

        if count == k:
            reverseHead = self._reverseKNodes(head, k)
            head.next = self.reverseNodesInKGroupV0(pointer, k)
            return reverseHead
        return head

    def _reverseKNodes(self, linkedNode: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        T: O(K)
        S: O(1)
        :param linkedNode:
        :param k:
        :return:
        """
        revHead, currNode = None, linkedNode

        while k:
            nextNode = currNode.next
            currNode.next = revHead
            revHead = currNode
            currNode = nextNode
            k -= 1
        return revHead
