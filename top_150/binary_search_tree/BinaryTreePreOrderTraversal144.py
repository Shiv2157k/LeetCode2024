from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def preOrderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        node = root
        output = []

        while node:

            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                pred = node.left

                while pred.right and pred.right != node:
                    pred = pred.right

                if not pred.right:
                    output.append(node.val)
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None
                    node = node.right
        return output

    def preOrderTraversalV1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Iterative Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        preorder, stack = [], [root, ]

        while stack:

            node = stack.pop()

            if node:
                preorder.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return preorder

    def preOrderTraversalV0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        return [root.val] + self.preOrderTraversal(root.left) + self.preOrderTraversal(root.right) if root else []
