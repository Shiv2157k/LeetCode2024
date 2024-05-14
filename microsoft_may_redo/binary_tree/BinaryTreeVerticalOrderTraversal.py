from typing import Optional, List
from collections import deque
from math import inf


class TreeNode:

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right



class BinaryTree:

    def vertical_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach:
        T: O()
        S: O()
        :param root:
        :return:
        """
        if not root:
            return []

        queue = deque([(root, 0)])
        left_boundary = inf
        right_boundary = -inf
        grid = {}

        while queue:

            node, col = queue.popleft()

            if node:

                grid[col] = grid.get(col, [])
                grid[col].append(node.val)

                left_boundary = min(left_boundary, col)
                right_boundary = max(right_boundary, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        output = []
        for col in range(left_boundary, right_boundary + 1):
            group = []
            for val in grid[col]:
                group.append(val)
            output.append(group)
        return output

