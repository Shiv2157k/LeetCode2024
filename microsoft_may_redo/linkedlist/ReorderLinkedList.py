from typing import Optional


class ListNode:

    def __init__(self, val: int=0, next: 'ListNode'=None):
        self.val = val
        self.next = next


class LinkedList:


    def reorder_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: two pointers
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head:
            return head

        fast = head
        slow = head
        # 1: find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2: reverse from mid
        prev, mid = None, slow
        while mid:
            next_node = mid.next
            mid.next = prev
            prev = mid
            mid = next_node

        first = head
        second = prev
        # 3. connect head and reverse mid alternatively
        while second.next:

            # first.next, first = second, first.next
            # second.next, second = first, second.next

            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
