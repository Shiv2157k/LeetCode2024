from typing import Optional


class ListNode:

    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def add_two_number_ii(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        T: O()
        S: O()
        :param l1:
        :param l2:
        :return:
        """

        r1 = self.__reverse(l1)
        r2 = self.__reverse(l2)
        carry = 0

        l3 = ListNode(-1)

        while r1 or r2 or carry:
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0

            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10

            head = ListNode(carry)
            l3.val = curr_sum % 10
            head.next = l3
            l3 = head

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None

        return l3.next if carry == 0 else l3

    def __reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param node:
        :return:
        """

        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
