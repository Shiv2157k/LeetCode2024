from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.front_node = None

    def is_palindrome_v1(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Reverse from mid
        T: O(N)
        S: O(1)
        Advanced with constant Space
        :param head:
        :return:
        """
        if not head:
            return True
        left_half_end = self.find_mid(head)
        second_half = self.reverse(left_half_end.next)

        result = True
        left = head
        right = second_half
        while right and result:
            if left.val != right.val:
                result = False
            left = left.next
            right = right.next

        # reverse the second half
        left_half_end.next = self.reverse(second_half)
        return result

    def find_mid(self, node: ListNode) -> ListNode:
        fast = node
        slow = node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, node: ListNode) -> ListNode:
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def is_palindrome_v0(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """
        self.front_node = head

        def recurse(node:Optional[ListNode] = head) -> bool:
            # base case
            if node:
                if not recurse(node.next):
                    return False
                if self.front_node.val != node.val:
                    return False
                self.front_node = self.front_node.next
            return True

        return recurse()
