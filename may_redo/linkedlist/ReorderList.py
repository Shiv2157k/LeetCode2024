from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reorder_list(self, head: Optional[ListNode]) -> None:

        if not head:
            return head

        fast = head
        slow = head

        # Step 1: find the mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse from the mid
        mid = slow
        prev = None

        while mid:
            next_node = mid.next
            mid.next = prev
            prev = mid
            mid = next_node

        # Step 3 Connect head and reverse mid alternatively
        first = head
        second = prev

        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

            # first.next, first = second, first.next
            # second.next, second = first, second.next
