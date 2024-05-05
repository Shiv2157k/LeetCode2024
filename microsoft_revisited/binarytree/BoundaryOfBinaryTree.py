from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.boundaries: List[int] = []

    def boundary_of_binary_tree_v1(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        self.boundaries = []

        if not root:
            return self.boundaries

        # add root
        if not self._is_leaf(root):
            self.boundaries.append(root.val)

        # add leftmost nodes
        pointer = root.left
        while pointer:

            if not self._is_leaf(pointer):
                self.boundaries.append(pointer.val)

            if pointer.left:
                pointer = pointer.left
            else:
                pointer = pointer.right

        # add leaf nodes
        self._add_leaf_nodes(root)

        # add right most nodes
        stack: List[int] = []
        pointer = pointer.right
        while pointer:

            if not self._is_leaf(pointer):
                stack.append(pointer.val)

            if pointer.right:
                pointer = pointer.right
            else:
                pointer = pointer.left

        while stack:
            self.boundaries.append(stack.pop())
        return self.boundaries

    def _add_leaf_nodes(self, node: Optional[TreeNode]) -> None:

        if not node:
            return

        if self._is_leaf(node):
            self.boundaries.append(node.val)
        else:
            for child in (node.left, node.right):
                if child:
                    self._add_leaf_nodes(child)

    def boundary_of_binary_tree_v0(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if root:
            self.boundaries.append(root.val)

        self._add_left_boundaries(root.left, True)
        self._add_right_boundaries(root.right, True)

        return self.boundaries

    def _is_leaf(self, node: Optional['TreeNode']):
        return not node.left and not node.right

    def _add_left_boundaries(self, node: Optional[TreeNode], is_boundary):

        if not node:
            return

        is_leaf: bool = self._is_leaf(node)

        if is_boundary or is_leaf:
            self.boundaries.append(node.val)

        if is_leaf:
            self._add_left_boundaries(node.left, is_boundary)
            self._add_right_boundaries(node.right, is_boundary and not node.left)

    def _add_right_boundaries(self, node: Optional[TreeNode], is_boundary):

        if not node:
            return

        is_leaf: bool = self._is_leaf(node)

        if not is_leaf:
            self._add_right_boundaries(node.left, is_boundary and not node.right)
            self._add_right_boundaries(node.right, is_boundary)

        if is_boundary or is_leaf:
            self.boundaries.append(node.val)
