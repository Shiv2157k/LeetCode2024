from typing import Optional


class ListNode:

    def __init__(self, val: int=-1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def getIntersectionNodeV1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None

        runner1, runner2 = headA, headB

        while runner1 != runner2:
            runner1 = runner1.next if runner1 else headB
            runner2 = runner2.next if runner2 else headA
        return runner1

    def getIntersectionNodeV0(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Approach: HashSet
        T: O(N)
        S: O(N)
        :param headA:
        :param headB:
        :return:
        """

        if not headB or not headA:
            return None

        visited = set()

        while headA:
            visited.add(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        return None
