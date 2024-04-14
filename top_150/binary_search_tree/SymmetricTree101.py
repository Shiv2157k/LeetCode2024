from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SymmetricTree:

    def isSymmetricV1(self, root: Optional[TreeNode]):
        """
        Approach: BFS
        T: O(H)
        S: O(H)
        :param root:
        :return:
        """

        queue = deque()
        queue.append((root.left, root.right))

        def isValid(left, right):

            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return True

        while queue:

            left, right = queue.popleft()

            if not isValid(left, right):
                return False

            if left:
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
        return True



    def isSymmetricV0(self, root: Optional[TreeNode]):
        """
        Approach: Depth First Search
        T: O(H)
        S: O(H)
        :param root:
        :return:
        """
        def dfs(leftNode, rightNode):

            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False

            return dfs(leftNode.left, rightNode.right) and dfs(leftNode.right, rightNode.left)

        return dfs(root.left, root.right)
