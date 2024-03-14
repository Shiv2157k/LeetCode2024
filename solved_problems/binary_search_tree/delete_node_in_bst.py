from typing import Optional

class TreeNode:

    def __init__(self, val: int = 0, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def successor(self, root: Optional[TreeNode]) -> int:
        # once right and then complete left until leaf node is reached.
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: Optional[TreeNode]) -> int:
        # one left and then complete right until leaf node is reached.
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNodeByKey(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Recursion
        Time Complexity: O(log N)
        Space Complexity: O(H)
        H -> Height of the tree
        :param root:
        :param key:
        :return:
        """

        # base case
        if not root:
            return None

        # if key is greater than the current node -> move right
        if key > root.val:
            root.right = self.deleteNodeByKey(root.right, key)
        # if key is less than the current node -> move left
        elif key < root.val:
            root.left = self.deleteNodeByKey(root.left, key)
        # if we found the key
        else:
            # case 1: if it is a leaf node
            if not (root.left or root.right):
                root.val = None
            # case 2: if there is right node -> set the successor
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNodeByKey(root.right, root.val)
            # case 3: if there is left node -> set the predecessor
            elif root.left:
                root.left = self.predecessor(root)
                root.left = self.deleteNodeByKey(root.left, root.val)

        return root


if __name__ == "__main__":

    t1 = TreeNode(7)
    t1.left = TreeNode(6)
    t1.right = TreeNode(9)
    t1.left.left = TreeNode(4)
    t1.right.left = TreeNode(5)
    t1.right.left = TreeNode(11)

    print(type(t1), t1.val, t1.left.val, t1.right.val)

    bst = BinarySearchTree()
    root = bst.deleteNodeByKey(t1, 9)

    while root:
        print(root.val)
        root = root.right

