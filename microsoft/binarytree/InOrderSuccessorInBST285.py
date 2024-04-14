from typing import Optional


class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    previous = None
    inOrderSuccessorNode = None

    def inOrderSuccessorV0(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach 1:
        T: O(N)
        S: O(N)
        :param root:
        :param p:
        :return:
        """
        self.previous = None
        self.inOrderSuccessorNode = None

        if p.right:
            leftmost = p.right

            while leftmost.left:
                leftmost = leftmost.left
            self.inOrderSuccessorNode = leftmost
        else:
            self._inOrderCaseTwo(root, p)
        return self.inOrderSuccessorNode

    def _inOrderCaseTwo(self, node: Optional[TreeNode], p: Optional[TreeNode]):

        if not node:
            return

        # recurse left tree
        self._inOrderCaseTwo(node.left, p)

        if self.previous == p and not self.inOrderSuccessorNode:
            self.inOrderSuccessorNode = p
            return

        self.previous = node
        self._inOrderCaseTwo(node.right, p)

    def inOrderSuccessorV1(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: BST rules
        T: O(N)
        S: O(1)
        :param root:
        :param p:
        :return:
        """

        successor = None

        while root:

            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

