from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_subtree_of_another(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Approach: DFS
        T: O(M * N)
        S: O(M + N)
        :param root:
        :param subRoot:
        :return:
        """

        def is_identical(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:

            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            return (node1.val == node2.val and
                    is_identical(node1.left, node2.left) and
                    is_identical(node1.right, node2.right))

        def dfs(node: Optional[TreeNode]) -> bool:

            if not node:
                return False
            elif is_identical(node, subRoot):
                return False

            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
