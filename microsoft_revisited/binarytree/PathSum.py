from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Approach: Iterative DFS
        T: O(N)
        S: O(N)
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:

            node, remain = stack.pop()
            if not node.left and not node.right and remain == 0:
                return True

            if node.left:
                stack.append((node.left, remain - node.left.val))
            if node.right:
                stack.append((node.right, remain - node.right.val))
        return False
