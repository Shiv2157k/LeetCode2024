from typing import Optional



class ListNode:


    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:


    def is_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Tortoise and hare
        t: O(N)
        S: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False