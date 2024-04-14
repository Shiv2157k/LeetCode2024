from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class InsertionSort:

    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Insertion Sort
        T: O(N)
        S:O(1)
        :param head:
        :return:
        """

        dummy = ListNode(-1)
        curr = head

        while curr:

            prev = dummy

            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            nextNode = curr.next
            # note: prev.next not prev
            curr.next = prev.next
            prev.next = curr

            curr = nextNode
        return dummy.next
