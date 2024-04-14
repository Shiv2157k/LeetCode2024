from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BoundaryOfBST:

    def getBoundaryOfBinaryTreeV1(self, root: Optional[TreeNode]):
        """
        Approach: Preorder Traversal
        :param root:
        :return:
        """

        result = []
        if root:
            result.append(root.val)

        self.addLeft(root.left, True, result)
        self.addRight(root.right, True, result)

    def addLeft(self, node: Optional[TreeNode], isBoundary: bool, result: List[int]):

        if not node:
            return
        isLeaf = self.isLeaf(node)

        if isBoundary or isLeaf:
            result.append(node.val)

        if not isLeaf:
            self.addLeft(node.left, isBoundary, result)
            self.addLeft(node.right, isBoundary and not node.left, result)

    def addRight(self, node: Optional[TreeNode], isBoundary: bool, result: List[int]):

        if not node:
            return

        isLeaf = self.isLeaf(node)

        if not isLeaf:
            self.addRight(node.left, isBoundary and not node.right, result)
            self.addRight(node.right, isBoundary, result)

        if isBoundary or isLeaf:
            result.append(node.val)

    def getBoundaryOfBinaryTreeV0(self, root: Optional[TreeNode]):
        """
        Approach: Three Steps
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        result = []
        # base cases
        if not root:
            return result

        if not self.isLeaf(root):
            result.append(root.val)

        # Three Steps

        # 1. capture all the left most nodes
        pointer = root.left
        while pointer:

            if not self.isLeaf(pointer):
                result.append(pointer.val)
            if pointer.left:
                pointer = pointer.left
            else:
                pointer = pointer.right

        # 2. capture all the leaf nodes
        self.addLeafNodes(result, root)

        # 3. capture all the right most nodes
        pointer = root.right
        stack = []
        while pointer:
            if not self.isLeaf(pointer):
                stack.append(pointer.val)
            if pointer.right:
                pointer = pointer.right
            else:
                pointer = pointer.left

        while stack:
            result.append(stack.pop())
        return result

    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        return not node.left and not node.right

    def addLeafNodes(self, result: List[int], node: Optional[TreeNode]) -> None:

        if self.isLeaf(node):
            result.append(node.val)
        else:
            if node.left:
                self.addLeafNodes(result, node.left)
            if node.right:
                self.addLeafNodes(result, node.right)
