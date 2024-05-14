from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def inorder_traversal_v2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        pointer = root
        inorder = []

        while pointer:

            if pointer.left:

                predecessor = pointer.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = pointer
                temp = pointer
                pointer = pointer.left
                temp.left = None
            else:
                inorder.append(pointer.val)
                pointer = pointer.right
        return inorder


    def inorder_traversal_v1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        inorder = []
        stack = []

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            inorder.append(root.val)

            root = root.right
        return inorder



    def inorder_traversal_v0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion V1
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        return self.inorder_traversal_v0(root.left) + [root.val] + self.inorder_traversal_v0(root.right) if root else []