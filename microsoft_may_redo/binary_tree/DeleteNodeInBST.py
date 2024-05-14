from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:


    def __sucessor(self, root: Optional[TreeNode]) -> int:
        node = root.right
        while node.left:
            node = node.left
        return node.val

    def __predecessor(self, root: Optional[TreeNode]) -> int:
        node = root.left
        while node.right:
            node = node.right
        return node.val

    def delete_node_in_bst(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Approach: Successor and Predecessor replacement
        T: O(log N)
        S: O(H)
        :param root:
        :param key:
        :return:
        """
        if not root:
            return None

        if root.val > key: # go left
            root.left = self.delete_node_in_bst(root.left, key)
        elif root.val < key: # go right
            root.right = self.delete_node_in_bst(root.right, key)
        else:
            
            # if it is a leaf simply delete
            if not root.right or not root.left:
                root = None
            elif root.left: # set predecessor
                root.val = self.__predecessor(root)
                root.left = self.delete_node_in_bst(root.left, root.val)
            elif root.right: # set successor
                root.val = self.__sucessor(root)
                root.right = self.delete_node_in_bst(root.right, root.val)
        return root

