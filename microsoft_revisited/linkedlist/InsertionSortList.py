from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        preHead = ListNode(-1)
        ptr = head

        while ptr:
            prev = preHead

            while prev.next and prev.next.val <= ptr.val:
                prev = prev.next

            nextNode = ptr.next
            ptr.next = prev.next
            prev.next = ptr

            ptr = nextNode
        return preHead.next
