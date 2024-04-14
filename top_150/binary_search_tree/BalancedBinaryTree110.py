from typing import Optional


class TreeNode:


    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def _height(self, root: Optional[TreeNode]) -> int:

        if not root:
            return - 1
        return 1 + max(self._height(root.left), self._height(root.right))

    def isBalancedV0(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion
        T: O(N log N)
        S: O(N)
        :param root:
        :return:
        """

        # base case
        if not root:
            return True

        return (abs(self._height(root.left) - self._height(root.right)) < 2
                and self.isBalancedV0(root.left)
                and self.isBalancedV0(root.right))

    def _isBalancedHelper(self, root: Optional[TreeNode]) -> (bool, int):

        if not root:
            return True, -1

        isLeftBalanced, leftHeight = self._isBalancedHelper(root.left)

        if not isLeftBalanced:
            return False, 0
        isRightBalanced, rightHeight = self._isBalancedHelper(root.right)
        if not isRightBalanced:
            return False, 0

        return (abs(rightHeight - leftHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalancedV1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Bottom-up recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        return self._isBalancedHelper(root)[0]