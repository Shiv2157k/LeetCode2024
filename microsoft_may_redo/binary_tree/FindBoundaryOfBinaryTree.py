from typing import Optional, List

[int]


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_boundary(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach:
        T: O()
        S: O()
        :param root:
        :return:
        """

        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        boundary = [root.val]

        node = root.left

        while node:

            if not self.__is_leaf_node(node):
                boundary.append(node.val)

            if node.left:
                node = node.left
            else:
                node = node.right

        self.__add_leaf_nodes(root, boundary)

        stack = []
        node = node.right

        while node:

            if not self.__is_leaf_node(node):
                stack.append(node.val)

            if node.right:
                node = node.right
            else:
                node = node.left

        while stack:
            boundary.append(stack.pop())
        return boundary

    def __add_leaf_nodes(self, node: Optional[TreeNode], boundary: List[int]):

        if not node:
            return

        if self.__is_leaf_node(node):
            boundary.append(node.val)
        else:
            self.__add_leaf_nodes(node.left, boundary)
            self.__add_leaf_nodes(node.right, boundary)

    def __is_leaf_node(self, node: Optional[TreeNode]):
        return not node.left and not node.right
