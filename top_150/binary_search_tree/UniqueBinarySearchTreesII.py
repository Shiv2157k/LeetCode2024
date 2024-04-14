from typing import List, Optional


class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def generateUniqueTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Approach: Recursion
        T: O(4^n / sqrt(n))
        S: O(E(n, k - 1) [(n - k + 1) * 4^k / sqrt(k)])
        -----------------------------------------------------------
        Intuition:
        n = 3
        Step1:                 Step 2:         Step 3:
        left SubTree Size  |  root values   | right SubTree Size
        -----------------------------------------------------------
            0              | '1'  2   3     |     2
            1              | 1   '2'  3     |     1
            2              | 1   2   '3'    |     0
        ------------------------------------------------------------
        * left will be from (i - 1)
        * right will be from (n - i)
        ------------------------------------------------------------
        :param n:
        :return:
        """

        memo = [[] for _ in range(n + 1)]
        return self.recurseWithMemo(n, memo)

    def recurseWithMemo(self, n: int, memo: List[List[int]]):

        if n == 0:
            return [None]
        if memo[n]:
            return memo[n]

        result = []

        for i in range(1, n + 1):

            left = self.recurseWithMemo(i - 1, memo)
            r = self.recurseWithMemo(n - i, memo)

            right = []

            for rightNode in r:
                right.append(self.changeVal(rightNode, i))

            for leftNode in left:
                for rightNode in right:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode
                    result.append(root)
        memo[n] = result
        return memo[n]

    def changeVal(self, root: Optional[TreeNode], i: int) -> Optional[TreeNode]:

        if not root:
            return None

        # Create new tree with updated values
        newRoot = TreeNode(root.val + i)
        newRoot.right = self.changeVal(root.left, i)
        newRoot.left = self.changeVal(root.right, i)
        return newRoot




