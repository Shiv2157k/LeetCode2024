from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(log N)
        S: O(H)
        :param root:
        :param key:
        :return:
        """

        if not root:
            return None

        if root.val > key:  # go left
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:  # go right
            root.right = self.deleteNode(root.right, key)
        else:  # root.val == key

            # if the node to delete is root node
            if not root.left and not root.right:
                root = None
            elif root.left:  # call the predecessor
                root.val = self._predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

            elif root.right:  # call the successor
                root.val = self._successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root

    def _successor(self, node: Optional[TreeNode]) -> int:

        node = node.right
        while node.left:
            node = node.left
        return node.val

    def _predecessor(self, node: Optional[TreeNode]) -> int:

        node = node.left
        while node.right:
            node = node.right
        return node.val
