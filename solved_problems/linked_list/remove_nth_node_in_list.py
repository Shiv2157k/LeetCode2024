from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_nth_element(self, head: Optional[ListNode], n: int):
        """
        One Pass
        T: O(L)
        S: O(1)
        :param head:
        :param n:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head
        first = second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

    def remove_nth_element(self, head: Optional[ListNode], n: int):
        """
        Two Pass
        T: O(L)
        S: O(1)
        :param head:
        :param n:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        size = 0

        while first:
            size += 1
            first = first.next

        size -= n
        first = dummy

        while size > 0:
            size -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next
