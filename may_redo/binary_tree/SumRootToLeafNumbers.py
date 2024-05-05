from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def sum_to_leaf_number_v2(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Morris Traversal
        T: O(N)
        S: O(1)
        :param root:
        :return:
        """

        root_to_leaf_sum = 0
        curr_number = 0

        while root:

            if root.left:
                predecessor = root.left
                steps = 1

                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    steps += 1

                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:
                    if predecessor.left is None:
                        root_to_leaf_sum += curr_number
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right
            else:

                curr_number = curr_number * 10 + root.val
                if root.right is None:
                    root_to_leaf_sum += curr_number
                root = root.right

        return root_to_leaf_sum

    def sum_to_leaf_number_v1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Iterative Stack
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        stack = [(root, 0)]
        root_to_leaf_sum = 0

        while stack:

            node, curr_number = stack.pop()
            if node:
                curr_number = curr_number * 10 + node.val

                if not node.left and not node.right:
                    root_to_leaf_sum += curr_number
                else:
                    stack.append((node.left, curr_number))
                    stack.append((node.right, curr_number))
        return root_to_leaf_sum

    def sum_to_leaf_number_v0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        def pre_order(node: Optional[TreeNode], curr_number: int):
            nonlocal root_to_leaf_sum

            if node:
                # calculate curr_number
                curr_number = curr_number * 10 + node.val

                # if leaf encountered add curr_number to leaf
                if not node.left and not node.right:
                    root_to_leaf_sum += curr_number
                pre_order(node.left, curr_number)
                pre_order(node.right, curr_number)

        root_to_leaf_sum = 0
        pre_order(root, 0)
        return root_to_leaf_sum
