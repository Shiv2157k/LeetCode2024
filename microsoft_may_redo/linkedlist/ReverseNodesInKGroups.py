from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_nodes_in_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :param head:
        :return:
        """

        new_head = None
        k_tail = None
        pointer = head

        while pointer:

            pointer = head
            count = 0

            while pointer and count < k:
                pointer = pointer.next
                count += 1

            if count == k:

                rev_head = self.__reverse(head, k)

                if not new_head:
                    new_head = rev_head

                if k_tail:
                    k_tail.next = rev_head

                k_tail = head
                head = pointer

        if k_tail:
            k_tail.next = head
        return new_head if new_head else head

    def __reverse(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:

        rev_head = None
        while node and k:
            next_node = node.next

            node.next = rev_head
            rev_head = node

            node = next_node
            k -= 1
        return rev_head
