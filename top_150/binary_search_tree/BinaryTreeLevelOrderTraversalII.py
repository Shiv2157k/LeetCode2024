from typing import Optional, List, Deque
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def levelOrderBottomV0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Recursion with Pre-order traversal root->left-> right
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        levels = []

        def preOrderDfs(node: Optional[TreeNode], level: int) -> None:

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            for nextNode in [node.left, node.right]:
                if nextNode:
                    preOrderDfs(nextNode, level + 1)

        preOrderDfs(root, 0)
        return levels

    def levelOrderBottomV1(self, root: Optional[TreeNode]) -> Deque[List[int]]:
        """
        Approach: Two Deque BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        levels = deque()
        queue = deque([root])

        while queue:

            level = []
            size = len(queue)
            for _ in range(size):
                root = queue.popleft()

                level.append(root.val)
                for nextNode in [root.left, root.right]:
                    if nextNode:
                        queue.append(nextNode)
            levels.appendleft(level)
        return levels


if __name__ == "__main__":

    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    bst = BinaryTree()
    print(bst.levelOrderBottomV1(t))
