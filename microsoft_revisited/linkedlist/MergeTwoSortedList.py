from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def mergeTwoLinkedListV1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O (M + N)
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """

        preHead = ListNode(-1)
        prev = preHead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return preHead.next

    def mergeTwoLinkedListV0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O (M + N)
        S: O(N)
        :param l1:
        :param l2:
        :return:
        """

        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLinkedListV1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLinkedListV1(l1, l2.next)
            return l2
