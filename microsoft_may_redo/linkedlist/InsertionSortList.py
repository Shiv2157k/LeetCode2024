from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def insertion_sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Insertion Sort List
        T: O(N^2)
        S: O(1)
        :param head:
        :return:
        """

        pre_head = ListNode(-1)
        pointer = head

        while pointer:
            prev = pre_head
            while prev.next and prev.next.val <= pointer.val:
                prev = prev.next

            next_node = pointer.next
            pointer.next = prev.next
            prev.next = pointer

            pointer = next_node
        return pre_head.next
