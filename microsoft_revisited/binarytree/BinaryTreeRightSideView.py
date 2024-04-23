from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def rightSideViewV1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: BFS
        T: O(N)
        S: O(1)
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

    def rightSideViewV0(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        rightSide = []

        def helper(node: TreeNode, level: int) -> None:

            if level == len(rightSide):
                rightSide.append(node.val)

            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightSide
