from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def verticalOrderTraversalSortByRow(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS using queue
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        grid = {}
        queue = deque([(root, 0, 0)])
        leftMost, rightMost = 0, 0

        while queue:

            node, row, col = queue.popleft()

            if node:
                grid[col] = grid.get(col, [])
                grid[col].append((row, node.val))

                leftMost = min(leftMost, col)
                rightMost = max(rightMost, col)

                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        output = []

        for col in range(leftMost, rightMost + 1):
            order = []
            for row, val in sorted(grid[col]):
                order.append(val)
            output.append(order)
        return output
