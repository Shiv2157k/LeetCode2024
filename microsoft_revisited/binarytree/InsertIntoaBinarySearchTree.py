from typing import Optional




class TreeNode:

    def __init__(self, val: int=-1, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def insert_into_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(H)
        S: O(H)
        :param root:
        :param val:
        :return:
        """
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insert_into_bst(root.right, val)
        else:
            root.left = self.insert_into_bst(root.left, val)
        return root


    def insert_into_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Iteration
        T: O(H)
        S: O(1)
        :param root:
        :param val:
        :return:
        """

        if not root:
            return TreeNode(val)

        pointer = root
        while pointer:
            if val > pointer.val:
                if not pointer.right:
                    pointer.right = TreeNode(val)
                    return root
                else:
                    pointer = pointer.right
            else:
                if not pointer.left:
                    pointer.left = TreeNode(val)
                    return root
                else:
                    pointer = pointer.left
        return TreeNode(val)

