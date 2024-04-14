from typing import Optional



class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def hasPathSumV1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSumV1(root.left, targetSum) or self.hasPathSumV1(root.right, targetSum)

    def hasPathSumV1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Approach: Iterative DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:

            node, remainSum = stack.pop()

            if not node.left and not node.right and remainSum == 0:
                return True
            if node.left:
                stack.append((node.left, remainSum - node.left.val))
            if node.right:
                stack.append((node.right, remainSum - node.right.val))
        return False