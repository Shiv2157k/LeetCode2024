from typing import List, Optional


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class LinkedList:

    def convert_to_binary_tree_v1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion with binary search
        T: O(N)
        S: O(N)
        :param head:
        :return:
        """

        size = self.__find_size(head)

        def convert(left: int, right: int) -> Optional[TreeNode]:
            nonlocal head

            if left > right:
                return None

            pivot = left + (right - left) // 2

            left = convert(left, pivot - 1)
            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = convert(pivot + 1, right)
            return node

        return convert(0, size - 1)

    def __find_size(self, node: Optional[ListNode]) -> int:
        size = 0
        while node:
            node = node.next
            size += 1
        return size

    def convert_to_binary_tree_v0(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        mid = self.__find_mid(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.convert_to_binary_tree_v0(head)
        node.right = self.convert_to_binary_tree_v0(mid.next)
        return node

    def __find_mid(self, node: Optional[ListNode]):
        slow = node
        fast = node
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
