from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, left: 'ListNode' = None):
        self.val = val
        self.left = left


class LinkedList:

    def odd_even_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
