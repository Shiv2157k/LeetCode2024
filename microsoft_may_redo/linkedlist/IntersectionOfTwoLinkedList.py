from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def intersection_of_two_linked_list(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Runners
        T: O(N)
        S: O(1)
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None

        runner1 = headA
        runner2 = headB

        while runner1 != runner2:
            runner1 = runner1.next if runner1.next else headB
            runner2 = runner2.next if runner2.next else headA
        return runner1