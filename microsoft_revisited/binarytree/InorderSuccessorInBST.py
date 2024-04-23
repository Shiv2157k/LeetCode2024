from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def inorder_successor(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(1)
        :param root:
        :param p:
        :return:
        """
        if not root or not p:
            return None

        successor = None

        while root:

            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
