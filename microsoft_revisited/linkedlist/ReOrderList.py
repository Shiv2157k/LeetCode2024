from typing import Optional


class ListNode:

    def __init__(self, val: int = - 1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reOrderList(self, head: Optional[ListNode]) -> None:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head:
            return head

        # step 1: Find middle and break into two halves
        fast = head
        slow = head

        while fast and fast.next:
            # prev = slow
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse from mid
        prev, mid = None, slow
        while mid:
            nextNode = mid.next
            mid.next = prev
            prev = mid
            mid = nextNode

        # Step 3: connect head and reverse mid
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
            # first.next, first = second, first.next
            # second.next, second = first, second.next
