from typing import Optional

class ListNode:

    def __init__(self, val:int=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:


    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        before = beforeHead = ListNode()
        after = afterHead = ListNode()

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = afterHead.next

        return beforeHead.next


if __name__ == "__main__":

    l1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

    ll = LinkedList()
    l2 = ll.partition(l1, 3)
    while l2:
        print(l2.val, end="->")
        l2 = l2.next
    print("\n")