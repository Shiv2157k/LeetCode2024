from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def detect_cycle_v0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        node_set = set()
        prev = head

        while prev:
            if prev in node_set:
                return prev
            node_set.add(prev)
            prev = prev.next
        return None

    def detect_cycle_v1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Fast and slow pointers
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        if not head and not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
