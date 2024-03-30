from typing import Optional


class ListNode:

    def __init__(self, val: int=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def removeNthNodeFromEndOfListV1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach: One Pass
        T: O(N)
        S: O(N)
        :param head:
        :param n:
        :return:
        """

        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


    def removeNthNodeFromEndOfListV0(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach: Two Pass
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        dummy = ListNode(-1)
        dummy.next = head
        preview = dummy

        size = -1

        while preview:
            size += 1
            preview = preview.next

        size = size - n
        preview = dummy
        while size:
            size -= 1
            preview = preview.next

        preview.next = preview.next.next
        return dummy.next


if __name__ == "__main__":
    linkedList = LinkedList()

    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    testl1 = l1

    l2 = linkedList.removeNthNodeFromEndOfListV0(testl1, 2)
    while l2:
        print(l2.val, end='->')
        l2 = l2.next
    print("\n")

    l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    testl2 = l3
    l4 = linkedList.removeNthNodeFromEndOfListV0(testl2, 2)
    while l4:
        print(l4.val, end='->')
        l4 = l4.next



