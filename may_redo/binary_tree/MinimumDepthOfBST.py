from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def min_depth_v1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Queue BFS
        T: O(N)
        S: O(min(H))
        :param root:
        :return:
        """
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

    def min_depth_v0(self, root: Optional[TreeNode]) -> int:

        def depth_first_search(node: Optional[TreeNode]) -> int:

            if not root:
                return 0

            if not root.left:
                return 1 + depth_first_search(root.right)
            if not root.right:
                return 1 + depth_first_search(root.left)
            return 1 + min(depth_first_search(root.left), depth_first_search(root.right))

        return depth_first_search(root)
