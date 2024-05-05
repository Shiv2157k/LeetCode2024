from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def to_linked_list(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        if not root:
            return None

        node = root
        while node:

            if node.left:

                predecessor = node.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = node.right
                node.right = node.left
                node.left = None
            else:
                node = node.right
