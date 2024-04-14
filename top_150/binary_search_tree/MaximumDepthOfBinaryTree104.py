from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def maxDepthV1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1

    def maxDepthV0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return depth
