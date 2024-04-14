from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def detectCycleV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Floyd's Cycle finding algorithm
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return None

        fast, slow = head, head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

    def detectCycleV0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """
        if not head or not head.next:
            return None

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
        return None
