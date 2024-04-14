from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach: DFS
        T: O(N)
        S: O(N) -> O(log N) average
        :param preorder:
        :param inorder:
        :return:
        """

        def arrayToTreeBuilder(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preOrderPointer

            if left > right:
                return None

            rootVal = preorder[preOrderPointer]
            preOrderPointer += 1
            root = TreeNode(rootVal)

            root.left = arrayToTreeBuilder(left, inOrderPointerMap[rootVal] - 1)
            root.right = arrayToTreeBuilder(inOrderPointerMap[rootVal] + 1, right)
            return root

        preOrderPointer = 0
        inOrderPointerMap = {}
        for pointer, value in enumerate(inorder):
            inOrderPointerMap[value] = pointer
        return arrayToTreeBuilder(0, len(preorder) - 1)
