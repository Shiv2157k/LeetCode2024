from typing import Optional


class ListNode:

    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
