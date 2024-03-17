from typing import Optional


class TreeNode:

    def __init__(self, val: int=-1):
        self.val = val
        self.left = None
        self.right = None


class BSTTraversal:

    def inorder_traversal(self, root: Optional[TreeNode]) -> TreeNode:
        """

        :param root:
        :return:
        """
        return self.traversal(root.left) + [root.val] + self.traversal(root.right) if root else []

    def pre_order_traversal(self, root: Optional[TreeNode]) -> TreeNode:
        return [root.val] + self.pre_order_traversal(root.left) + self.pre_order_traversal(root.right) if root else []

    def post_order_traversal(self, root: Optional[TreeNode]) -> TreeNode:
        return self.post_order_traversal(root.left) + self.pre_order_traversal(root.right) + [root.val] if root else []


