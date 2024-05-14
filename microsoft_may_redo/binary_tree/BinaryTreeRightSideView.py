from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_right_side_view_v0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        output = []

        def helper(node: Optional[TreeNode], level: int) -> None:

            if level == len(output):
                output.append(node.val)
            for child in (node.left, node.right):
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return output

    def get_right_side_view_v1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: BFS Queue
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        queue = deque([root])
        output = []

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                if i == size - 1:
                    output.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output
