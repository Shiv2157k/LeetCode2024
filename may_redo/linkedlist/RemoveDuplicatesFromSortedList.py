from collections import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """
        pointer = head

        while pointer and pointer.next:

            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head

