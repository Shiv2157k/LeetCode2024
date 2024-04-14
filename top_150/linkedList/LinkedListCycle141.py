from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Floyd's Cycle Finding Algorithm
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

    def hasCycleV1(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Floyd's Cycle Finding Algorithm
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
