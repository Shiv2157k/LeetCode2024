from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Approach: Iterative Stack
        T: O(N)
        S: O(N)
        :param root:
        :param target_sum:
        :return:
        """

        stack = [(root, target_sum - root.val)]

        while stack:
            node, remain = stack.pop()

            if not node.left and not node.right and remain == 0:
                return True

            if node.left:
                stack.append((node.left, remain - node.left.val))
            if node.right:
                stack.append((node.right, remain - node.right.val))
        return False
