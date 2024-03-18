from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def kth_smallest_element_v1(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param root:
        :param k:
        :return:
        """
        stack = []
        while k >= 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kth_smallest_element_v0(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :param k:
        :return:
        """

        def in_order(node: Optional[TreeNode]) -> List[int]:
            return in_order(node.left) + [node.val] + in_order(node.right) if node else []

        return in_order(root)[k - 1]

