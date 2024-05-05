from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:

    def __init__(self, val: int = -1, next: 'ListNode' = None):
        self.val = val
        self.next = next


class ListNodeToBinaryTree:

    def convert_v1(self, head: Optional[ListNode]):
        """
        Approach: Inorder Simulation
        T: O(N)
        S: O(log N)
        :param head:
        :return:
        """

        size = self._find_size(head)

        def to_bst(left: int, right: int) -> TreeNode:
            nonlocal head

            if left > right:
                return None

            pivot = (left + right) // 2

            # Step 1: simulate inorder for left half recursively
            left = to_bst(left, pivot - 1)

            node = TreeNode(head.val)
            node.left = left

            # Step 2: maintaining invariance
            head = head.next

            # Step 3: Recurse on the right half
            node.right = to_bst(pivot + 1, right)
            return node

        return to_bst(0, size - 1)

    def _find_size(self, head: Optional[ListNode]) -> int:
        ptr = head
        size = 0
        while ptr:
            ptr = ptr.next
            size += 1
        return size

    def convert_v0(self, head: Optional[ListNode]):
        """
        Approach: Mid as root - Recursion
        T: O(N log N)
        S: O(log N)
        :param head:
        :return:
        """

        if not head:
            return None

        mid = self._find_mid(head)
        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.convert_v0(head)
        node.right = self.convert_v0(mid.next)
        return node

    def _find_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None
        return slow
