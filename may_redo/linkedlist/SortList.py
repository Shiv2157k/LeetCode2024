from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        if not head:
            return None

        mid = self._mid_node(head)
        left = self.sort_list(head)
        right = self.sort_list(mid)
        sorted_list = self._merge_list(left, right)

        return sorted_list

    def _mid_node(self, node: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):

        fast = node.next
        slow = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def _merge_list(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        l3 = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        return dummy.next
