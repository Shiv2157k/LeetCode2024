from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def getVerticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        # validation
        if not root:
            return []

        grid = {}
        # node, level
        queue = deque([(root, 0)])
        leftMostCol, rightMostCol = 0, 0

        while queue:
            node, column = queue.popleft()

            if node:
                grid[column] = grid.get(column, [])
                grid[column].append(node.val)
                # gives the leftmost
                leftMostCol = min(leftMostCol, column)
                # gives the rightmost
                rightMostCol = max(rightMostCol, column)

                # decrement by 1 starting from root i.e., o
                queue.append((node.left, column - 1))
                # increment by 1 starting from root i.e., 0
                queue.append((node.right, column + 1))

        output = []
        # iterate leftmost ---> rightMost
        # add it from the grid we built
        for col in range(leftMostCol, rightMostCol + 1):
            output.append(grid[col])
        return output
