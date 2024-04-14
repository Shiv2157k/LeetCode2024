from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def reOrder(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        # Step 1: Find mid
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse from mid
        mid, prev = slow, None
        while mid:
            nextNode = mid.next
            mid.next = prev
            prev = mid
            mid = nextNode

        preHead = ListNode(-1)
        preHead.next = head
        prev = preHead

        # Step 3: from the beginning connect to
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            """
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
            """
