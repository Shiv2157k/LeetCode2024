from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def isCycleV1(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Floyd's Cycle
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def isCycleV0(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Set
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head or not head.next:
            return False

        visited = set()

        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
                curr = curr.next
            else:
                return True
        return False
