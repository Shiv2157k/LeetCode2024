from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def validate_binary_tree(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Inorder Traversal using stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = []
        prev = None

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev is not None and prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True
