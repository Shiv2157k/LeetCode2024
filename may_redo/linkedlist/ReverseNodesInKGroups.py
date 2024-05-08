from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_nodes_in_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach:
        T: O()
        S: O()
        :param head:
        :param k:
        :return:
        """
        if not head:
            return head

        new_head = None
        kTail = None
        pointer = head

        while pointer:
            count = 0
            pointer = head

            while pointer and count < k:
                pointer = pointer.next
                count += 1

            if count == k:

                rev_head = self._reverse_k_nodes(head, k)

                if not new_head:
                    new_head = rev_head

                if kTail:
                    kTail.next = rev_head

                kTail = head
                head = pointer

        if kTail:
            kTail.next = head
        return new_head if new_head else head


    def _reverse_k_nodes(self, node: Optional[ListNode], k: int):
        rev_head = None

        for _ in range(k):
            next_node = node.next
            node.next = rev_head
            rev_head = node
            node = next_node
        return rev_head
