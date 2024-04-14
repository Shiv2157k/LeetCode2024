from enum import Enum, auto
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class State:
    START = auto()
    END = auto()


class BinaryTree:

    def flattenToLinkedListV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """
        curr = root
        while curr:
            if curr.left:
                predecessor = curr.left

                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = curr.right
                    curr.right = curr.left
                    curr.left = None
            curr = curr.right
        return root

    def flattenToLinkedListV1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iteration  Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = [(root, State.START)]
        leftTail = None

        while stack:
            curr, state = stack.pop()

            # check for leaf node
            if not curr.left and not curr.right:
                leftTail = curr

            if state == State.START:

                if curr.left:
                    stack.append((curr, State.END))
                    stack.append((curr.left, State.START))
                elif curr.right:
                    stack.append((curr.right, State.END))
            else:

                rightNode = curr.right

                if leftTail:
                    leftTail.right = curr.right
                    curr.right = curr.left
                    curr.left = None

                if rightNode:
                    stack.append((rightNode, State.START))
        return root


    def _flattenedTreeVO(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Helper function for flattenToLinkedListV0
        :param root:
        :return:
        """

        # base case
        if not node:
            return None

        # if it is a leaf return the node which wil be left or right leaf
        if not node.left or not node.right:
            return node

        leftTail = self._flattenedTreeVO(node.left)
        rightTail = self._flattenedTreeVO(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        return rightTail if rightTail else leftTail

    def flattenToLinkedListV0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        return self._flattenedTreeV0(root)
