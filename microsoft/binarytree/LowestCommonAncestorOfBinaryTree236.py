from typing import Optional

class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    ans = None
    def lowestCommonAncestorV0(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

        def recurseTree(currNode: Optional[TreeNode]):

            if not currNode:
                return False

            left = recurseTree(currNode.left)
            right = recurseTree(currNode.right)

            mid = currNode == p or currNode == q

            if left + mid + right >= 2:
                self.ans = currNode
            return mid or left or right
        recurseTree(root)
        return self.ans

    def lowestCommonAncestorV1(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Stack Iterative
        T: O(N)
        S: O(N)
        :param root:
        :param p:
        :param q:
        :return:
        """

        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q