from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



class BinarySearchTree:


    def insertValIntoBSTV0(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(H)
        :param root:
        :param val:
        :return:
        """

        # base case
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertValIntoBSTV0(root.right, val)
        else:
            root.left = self.insertValIntoBSTV0(root.left, val)
        return root

    def insertValIntoBSTV1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach: Iteration
        T: O(N)
        S: O(H)
        :param root:
        :param val:
        :return:
        """

        node = root

        while node:

            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        return TreeNode(val)