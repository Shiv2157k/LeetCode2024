from typing import Optional


class ListNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LinkedLists:

    def addTwoNumbersV1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Using Stack
        T: O(M + N)
        S: O(M + N)
        :param l1:
        :param l2:
        :return:
        """
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        currSum = 0
        carry = 0
        l3 = ListNode()

        while stack1 or stack2:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0

            currSum = v1 + v2 + carry
            carry = currSum // 10

            l3.val = currSum % 10
            head = ListNode(carry)
            head.next = l3
            l3 = head
        return l3.next if carry == 0 else l3

    def addTwoNumbersV0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Reverse And Add
        T: O(M + N)
        S: O(M + N)
        :param l1:
        :param l2:
        :return:
        """

        r1 = self._reverse(l1)
        r2 = self._reverse(l2)
        # preHead = ListNode()
        # l3 = preHead

        l3 = ListNode()
        carry = 0

        while r1 or r2 or carry:
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0

            currSum = v1 + v2 + carry
            carry = currSum // 10

            # two ways to do
            # OneWay:
            # l3.next = ListNode(currSum % 10)
            # l3 = l3.next
            # Second Way:
            l3.val = currSum % 10
            head = ListNode(carry)
            head.next = l3
            l3 = head

            r1 = r1.next if r1 else None
            r2 = r2.next if r2 else None

        # return self._reverse(preHead.next)
        return l3.next if carry == 0 else l3

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None

        while node:
            nextNode = node.next
            node.next = newHead
            newHead = node
            node = nextNode
        return newHead
