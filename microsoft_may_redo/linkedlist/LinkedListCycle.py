from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def has_cycle(self, head: Optional['ListNode']) -> bool:
        """
        Approach: Floyd's Cycling Algo
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False