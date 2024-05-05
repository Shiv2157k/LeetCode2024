from typing import Optional, Deque
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def serialize_bst(self, root: Optional[TreeNode]) -> str:
        """
        Approach: PreOrder
        :param root:
        :return:
        """
        if not root:
            return ''

        queue: Deque[TreeNode] = deque([root])
        output = ''

        while queue:
            node = queue.popleft()

            if not node:
                output += 'None,'
            else:
                output += str(node.val) + ','
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output

    def deserialize_bst(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None

        iter_vals = iter(data.split(','))
        root = TreeNode(int(next(iter_vals)))
        queue: Deque[TreeNode] = deque([root])

        while queue:
            size = len(queue)
            for _ in range(size):
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
