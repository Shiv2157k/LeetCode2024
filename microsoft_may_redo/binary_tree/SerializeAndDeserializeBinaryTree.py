from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return ''
        queue = deque([root])
        serialized_data = []

        while queue:
            node = queue.popleft()

            if not node:
                serialized_data.append('None')
            else:
                serialized_data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(serialized_data)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param data:
        :return:
        """
        if not data:
            return None

        iter_vals = iter(data.split(','))
        root = TreeNode(int(next(iter_vals)))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            left = next(iter_vals)
            right = next(iter_vals)

            node.left = None if left == 'None' else TreeNode(int(left))
            node.right = None if right == 'None' else TreeNode(int(right))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
