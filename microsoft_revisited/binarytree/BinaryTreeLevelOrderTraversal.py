from typing import Optional, List
from collections import deque

class TreeNode:

    def __init__(self, val:int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BinarySearchTree:


    def levelOrderTraversalV1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        queue = deque([root])
        levels = []
        while queue:

            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels

    def levelOrderTraversalV0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        def traverse(node: Optional[TreeNode], level: int):

            if len(levels) == level:
                levels[level] = [node.val]
            else:
                levels[level].append(node.val)

            for nextNode in (node.left, node.right):
                if nextNode:
                    traverse(nextNode, level + 1)

        levels = []
        traverse(root, 0)
        return levels