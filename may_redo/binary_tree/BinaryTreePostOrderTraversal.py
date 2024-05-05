from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def post_order_vo(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        PostOrder: left -> right -> root
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        return self.post_order_vo(root.left) + self.post_order_vo(root.right) + [root.val] if root else []


    def post_order_v1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Iterative Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        stack = [(root, False)]
        output = []

        while stack:

            node, visited = stack.pop()
            
            if node:

                if visited:
                    output.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return output