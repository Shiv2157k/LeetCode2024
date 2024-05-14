from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def lowest_common_ancestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> \
            Optional[TreeNode]:
        """
        Approach: Iterative Stack, Dict and set
        T: O(N)
        S: O(N)
        :param root:
        :param p:
        :param q:
        :return:
        """

        if not root:
            return root

        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()
            for child_node in (node.left, node.right):
                if child_node:
                    stack.append(child_node)
                    parent[child_node] = node

        # add the parents of p into ancestor set
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q
