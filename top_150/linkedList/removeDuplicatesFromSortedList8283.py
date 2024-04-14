from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def deleteDuplicatesI(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Straight Forward
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        prev = head

        while prev and prev.next:
            if prev.val == prev.next.val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head

    def deleteDuplicatesII(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Sentinel Head + Predecessor
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        preHead = ListNode(-1, head)
        prev = preHead

        while head:

            if head.next and head.val == head.next.val:

                while head.next and head.val == head.next.val:
                    head = head.next

                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return preHead.next


if __name__ == "__main__":

    l1 = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(7, ListNode(9, ListNode(8, ListNode(8))))))))

    ll = LinkedList()
    l1 = ll.deleteDuplicatesII(l1)
    while l1:
        print(l1.val, end="->")
        l1 = l1.next
    print("\n")

    l2 = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(7, ListNode(9, ListNode(8, ListNode(8))))))))

    l12 = ll.deleteDuplicatesI(l2)
    while l12:
        print(l12.val, end="->")
        l12 = l12.next
