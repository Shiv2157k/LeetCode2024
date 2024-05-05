from typing import Optional, List, Dict, Tuple


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def vertical_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        left_most: int = 0
        right_most: int = 0
        grid: Dict[int, List[Tuple[int, int]]] = {}
        # node, col it is placed in
        stack: List[Tuple[TreeNode, int, int]] = [(root, 0, 0)]

        while stack:

            node, row, col = stack.pop()

            if node:

                left_most = min(left_most, col)
                right_most = max(right_most, col)

                grid[col] = grid.get(col, [])
                grid[col].append((row, node.val))

                if node.left:
                    stack.append((node.left, row + 1, col - 1))
                if node.right:
                    stack.append((node.right, row + 1, col + 1))

        result: List[List[int]] = []
        for col in range(left_most, right_most + 1):
            order: List[int] = []
            for row, val in sorted(grid[col]):
                order.append(val)
            result.append(order)
        return result
