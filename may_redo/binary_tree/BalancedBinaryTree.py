from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_balanced_height(self, root: Optional[TreeNode]) -> bool:
        def depth_first_search(node: Optional[TreeNode]) -> (bool, int):
            if not node:
                return True, 0

            left = depth_first_search(node.left)
            right = depth_first_search(node.right)

            is_balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return is_balance, 1 + max(left[1], right[1])

        return depth_first_search(root)[0]
