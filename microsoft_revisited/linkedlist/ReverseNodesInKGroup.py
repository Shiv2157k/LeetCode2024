from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def reverseNodesInKGroupV1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param head:
        :param k:
        :return:
        """
        newHead = None
        ktail = None

        ptr = head

        while ptr:

            ptr = head
            count = 0

            while ptr and count < k:
                count += 1
                ptr = ptr.next

            if count == k:

                revHead = self.reverseNodes(head, k)

                if not newHead:
                    newHead = revHead

                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        if ktail:
            ktail.next = head
        return newHead if newHead else head

    def reverseNodes(self, node: Optional[ListNode], k: int):
        prev = None
        while k:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
            k -= 1
        return prev

    def reverseNodesInKGroupV0(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        pointer = head
        count = 0

        while pointer and count < k:
            count += 1
            pointer = pointer.next

        if count == k:

            revHead = self.reverseNodes(head, k)

            head.next = self.reverseNodes(pointer, k)

            return revHead
        return head

