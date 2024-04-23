from typing import Optional, List, Dict, Deque, Tuple
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def vertical_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: HashMap and Queue
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        grid: Dict[int, List[int]] = {}
        queue: Deque[Tuple[TreeNode, int]] = deque([(root, 0)])
        left_most: int = 0
        right_most: int = 0

        while queue:

            node, col = queue.popleft()

            if node:
                grid[col] = grid.get(col, [])
                grid[col].append(node.val)

                left_most = min(left_most, col)
                right_most = max(right_most, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        output: List[List[int]] = []
        for col in range(left_most, right_most + 1):
            output.append(grid[col])
        return output
