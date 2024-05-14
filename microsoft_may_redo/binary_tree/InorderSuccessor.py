from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.__previous = None
        self.__inorder_successor_node = None
    def in_order_successor_v0(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        """
        Approach: Without using BST properties
        T: O(N)
        S: O(N)
        :param root:
        :param p:
        :return:
        """

        self.__previous = None
        self.__inorder_successor_node = None

        if p.right:
            leftmost = p.right

            while leftmost.left:
                leftmost = leftmost.left
            self.__inorder_successor_node = leftmost
        else:
            self.__inorder_case_two(root, p)
        return self.__inorder_successor_node

    def __inorder_case_two(self, node: Optional[TreeNode], p: Optional[TreeNode]):

        if not node:
            return

        self.__inorder_case_two(node.left, p)

        if self.__previous == p and not self.__inorder_successor_node:
            self.__inorder_successor_node= node
            return

        self.__previous = node
        self.__inorder_case_two(node.right, p)


    def in_order_successor_v1(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        """
        Approach: Using BST Properties
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        successor = None

        while root:

            if root.val > p.val:
                successor = root
                root = root.left
            elif root.val <= p.val:
                root = root.right
        return successor