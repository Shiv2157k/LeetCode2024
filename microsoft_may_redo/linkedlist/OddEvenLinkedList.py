from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def odd_even_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head:
            return head

        odd_ptr = head
        even_ptr = head.next
        even_head = head.next

        while even_ptr and even_ptr.next:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next

            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
        odd_ptr.next = even_head
        return head
