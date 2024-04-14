from typing import Optional



class ListNode:

    def __init__(self, val: int=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N log N)
        S: O(N)
        :param head:
        :return:
        """

        if not head or head.next:
            return head

        mid = self.getNodesAfterMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left, right)


    def getNodesAfterMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return mid

    def mergeList(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:

        preHead = ListNode(-1)
        pointer = preHead

        while left and right:
            if left.val <= right.val:
                pointer.next = left
                left = left.next
            else:
                pointer.next = right
                right = right.next
            pointer = pointer.next
        pointer.next = left or right
        return preHead.next