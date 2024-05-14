from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def insert_val_to_bst_v1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Inorder
        T: O(N)
        S: O(1)
        :param root:
        :param val:
        :return:
        """
        node = root
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                node = node.right
        return TreeNode(val)

    def insert_val_to_bst_v0(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(H)
        :param root:
        :param val:
        :return:
        """

        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insert_val_to_bst_v0(root.right, val)
        else:
            root.left = self.insert_val_to_bst_v0(root.left, val)
        return root
