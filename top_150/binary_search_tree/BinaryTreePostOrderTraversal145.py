from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def postOrderTraversalV0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        return self.postOrderTraversalV0(root.left) + self.postOrderTraversalV0(root.right) + [root.val] if root else []

    def postOrderTraversalV1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        output = []

        stack = [(root, False)]

        while stack:

            node, visited = stack.pop()

            if visited:
                output.append(node.val)
            else:
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return output


