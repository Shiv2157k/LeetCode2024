from typing import Optional, Dict, List, Set


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def lowestCommonAncestor(
            self,
            root: Optional[TreeNode],
            p: Optional[TreeNode],
            q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Approach: Set and Map
        T: O(N)
        S: O(N)
        :param root:
        :param p:
        :param q:
        :return:
        """

        if not root:
            return None

        stack: List[TreeNode] = [root]
        parent: Dict[TreeNode, TreeNode] = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            for child in (node.left, node.right):
                if child:
                    stack.append(child)
                    parent[child] = node

        ancestors: Set[TreeNode] = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q
