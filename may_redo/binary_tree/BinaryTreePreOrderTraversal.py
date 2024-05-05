from typing import Optional, List



class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right



class BinaryTree:

    def pre_order_vo(self, root: Optional['TreeNode']) -> List[int]:
        """
        Preorder: -> root -> left -> right
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        return [root.val] + self.pre_order_vo(root.left) + self.pre_order_vo(root.right) if root else []


    def pre_order_v1(self, root: Optional['TreeNode']) -> List[int]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        stack = [root]
        preorder = []

        while stack:
            root = stack.pop()

            if root:
                preorder.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return preorder


    def pre_order_v2(self, root: Optional['TreeNode']) -> List[int]:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """
        node = root
        preorder = []

        while node:

            if not node.left:
                preorder.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    preorder.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return preorder


