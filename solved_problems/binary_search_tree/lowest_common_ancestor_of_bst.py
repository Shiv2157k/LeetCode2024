from typing import Optional


class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def lowest_common_lca_v1(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(1)
        :param root:
        :param p:
        :param q:
        :return:
        """

        p_val = p.val
        q_val = q.val

        node = root

        while node:
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node

    def lowest_common_lca_v0(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        :param root:
        :param p:
        :param q:
        :return:
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowest_common_lca_v0(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowest_common_lca_v0(root.left, p, q)
        else:
            return root
