from typing import Optional


class ListNode:


    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:


    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        # sentinel head to avoid edge cases
        pre_head = ListNode(-1)
        pre_head.next = head
        pointer = pre_head

        while head:

            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pointer = head.next
            else:
                pointer = pointer.next
            head = head.next
        return pre_head.next