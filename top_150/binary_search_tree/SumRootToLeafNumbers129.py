from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def sumRootToLeafNodeV2(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        rootToLeaf, currNumber = 0, 0

        while root:

            if root.left:

                predecessor = root.left
                steps = 1

                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    steps += 1

                if predecessor.right is None:
                    currNumber = currNumber * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:

                    if predecessor.left is None:
                        rootToLeaf += currNumber

                    for _ in range(steps):
                        currNumber //= 10

                    predecessor.right = None
                    root = root.right
            else:

                currNumber = currNumber * 10 + root.val
                if root.right is None:
                    rootToLeaf += currNumber
                root = root.right
        return rootToLeaf

    def sumRootToLeafNodeV1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Preorder Iterative
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        rootToLeafSum = 0
        stack = [(root, 0)]

        while stack:
            node, currNum = stack.pop()

            if node:
                currNum = currNum * 10 + node.val

                if not node.left and not node.right:
                    rootToLeafSum += currNum
                else:
                    stack.append((node.left, currNum))
                    stack.append((node.right, currNum))
        return rootToLeafSum

    def sumRootToLeafNodeV0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Preorder Recursive
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        def preOrder(node: Optional[TreeNode], currNum: int) -> None:
            nonlocal rootToLeafSum
            if node:
                currNum = currNum * 10 + node.val

                if not node.left and not node.right:
                    rootToLeafSum += currNum
                else:
                    preOrder(node.left, currNum)
                    preOrder(node.right, currNum)

        rootToLeafSum = 0
        preOrder(root, 0)
        return rootToLeafSum
