from typing import Optional


class LinkedNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def re_order_list(self, head: Optional[LinkedNode]) -> None:
        """
        Approach: Reverse second part and merge two sorted list
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        fast = slow = head
        # Step 1: Find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        # Step 2: Reverse the second half
        while curr:
            # curr.next, curr = prev, curr.next
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr.next = next_node

        first, second = head, prev
        # Step 3: Merge them as per requirement
        while second.next:
            # first.next, first = second, first.next
            # second.next, second = first, second.next
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
