from typing import Optional


class LinkedNode:

    def __init__(self, val: int=-1, next=None):
        self.val = val
        self.next = next


class LinkedListCycle:

    def has_cycle_v1(self, head: Optional[LinkedNode]) -> bool:
        """
        Approach: Floyd's Cycle finding algorithm
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        # base case
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast != slow:

            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

    def has_cycle_v0(self, head: Optional[LinkedNode]) -> bool:
        """
        Approach: Hash Table
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """
        visited = set()
        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
                curr = curr.next
            else:
                return True
        return False