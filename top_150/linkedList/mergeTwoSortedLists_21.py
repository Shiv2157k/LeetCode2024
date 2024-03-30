from typing import Optional

class ListNode:

    def __init__(self, val:int=-1, next=None):
        self.val = val
        self.next = next

class LinkedListSorted:


    def mergeTwoSortedListV1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Iteration
        T: O(N)
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
        prev.next = l1 if l1 is not None else l2
        return preHead.next

    def mergeTwoSortedListV0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Recursion
        T: O(N + M)
        S: O(N + M)
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoSortedListV0(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedListV0(l1, l2.next)
            return l2


if __name__ == "__main__":
    linkedList = LinkedListSorted()

    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    testl1 = l1
    l11 = ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(7)))))
    testl11 = l11

    l2 = linkedList.mergeTwoSortedListV1(testl1, testl11)
    while l2:
        print(l2.val, end='->')
        l2 = l2.next
    print("\n")

    l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    testl2 = l3
    l33 = ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(7)))))
    testl33 = l33
    l4 = (linkedList
          .mergeTwoSortedListV0(testl2, testl33))
    while l4:
        print(l4.val, end='->')
        l4 = l4.next