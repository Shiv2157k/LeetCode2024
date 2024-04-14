from typing import Optional, List


class TreeNode:

    def __init__(self, val: int=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def listToTreeBuilder(left: int, right: int) -> Optional[TreeNode]:

            nonlocal postOrderPtr

            if left > right:
                return None

            rootVal = postorder[postOrderPtr]
            root = TreeNode(rootVal)
            postOrderPtr -= 1

            root.right = listToTreeBuilder(inOrderPtrMap[rootVal] + 1, right)
            root.left = listToTreeBuilder(left, inOrderPtrMap[root.val] - 1)
            return root

        postOrderPtr = len(postorder) - 1
        inOrderPtrMap = {}

        for index, val in enumerate(inorder):
            inOrderPtrMap[val] = index
        return listToTreeBuilder(0, len(inorder) - 1)