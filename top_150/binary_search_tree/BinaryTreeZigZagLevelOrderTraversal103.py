from collections import deque
from typing import List, Optional


class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ZigZag:


    def levelOrderV1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))

        levels = []

        while queue:
            currLevel = deque()
            size = len(queue)
            for _ in range(size):
                root, level = queue.popleft()

                if level % 2 == 1:
                    currLevel.appendleft(root.val)
                else:
                    currLevel.append(root.val)

                if root.left:
                    queue.append((root.left, level + 1))
                if root.right:
                    queue.append((root.right, level + 1))
            levels.append(currLevel)
        return levels

    def levelOrderV0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        result = []

        def dfs(node: Optional[TreeNode], level: int):

            if level == len(result):
                result.append(deque([node.val]))
            elif level % 2 == 1:
                result[level].appendleft(node.val)
            else:
                result[level].append(node.val)

            for nextNode in [node.left, node.right]:
                if nextNode:
                    dfs(nextNode, level + 1)
        dfs(root, 0)
        return result
