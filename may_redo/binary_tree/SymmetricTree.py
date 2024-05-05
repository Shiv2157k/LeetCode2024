from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_symmetric_tree_v0(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def is_symmetric(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:

            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            return is_symmetric(left_node.left, right_node.right) and is_symmetric(left_node.right, right_node.left)

        return is_symmetric(root.left, root.right)

    def is_symmetric_tree_v1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative Queue
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def is_valid(left, right):

            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return True

        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            left_node, right_node = queue.popleft()
            if not is_valid(left_node, right_node):
                return False

            if left_node:
                queue.append((left_node.left, right_node.right))
                queue.append((left_node.right, right_node.left))
        return True
