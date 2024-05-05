from typing import Optional, List


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class LinkedList:

    def add_two_numbers_v1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: School Back Addition with reverse
        T: O(N)
        S: O(1)
        :param l1:
        :param l2:
        :return:
        """

        r1 = self._reverse(l1)
        r2 = self._reverse(l2)

        carry: int = 0
        l3 = ListNode(-1)

        while r1 or r2 or carry:
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0

            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10
            # reverse the l3 here itself
            l3.val = curr_sum % 10
            head = ListNode(carry)
            head.next = l3
            l3 = head

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None
        return l3.next if carry == 0 else l3

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        rev_head = None
        while node:
            next_node = node.next
            node.next = rev_head
            rev_head = node
            node = next_node
        return rev_head

    def add_two_numbers_v0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Stack
        T: O(N)
        S: O(N + M)
        :param l1:
        :param l2:
        :return:
        """

        stack_1: List[int] = []
        stack_2: List[int] = []

        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        carry: int = 0
        l3 = ListNode(-1)

        while stack_1 or stack_2:
            v1 = stack_1.pop() if stack_1 else 0
            v2 = stack_2.pop() if stack_2 else 0

            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10

            l3.val = curr_sum % 10
            head = ListNode(carry)
            head.next = l3
            l3 = head
        return l3.next if carry == 0 else l3
