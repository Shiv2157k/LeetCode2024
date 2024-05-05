from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, left: 'ListNode' = None, right: 'ListNode' = None):
        self.val = val
        self.left = left
        self.right = right


class LinkedList:

    def insertion_sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Insertion Sort
        T: O(N^2)
        S: O(1)
        :param head:
        :return:
        """

        preHead = ListNode(-1)
        pointer = head

        while pointer:

            prev = preHead
            while prev.next and prev.next.val <= head.val:
                prev = prev.next

            next_node = pointer.next
            pointer.next = prev.next
            prev.next = pointer

            pointer = next_node
        return preHead.next
