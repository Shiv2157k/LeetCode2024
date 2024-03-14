from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def closest_tree_value_v2(self, root: Optional[TreeNode], target: int) -> float:
        """
        Approach: Binary Search
        T: O(H)
        S: O(1)
        :param root:
        :param target:
        :return:
        """
        closest = root.val
        while root:
            closest = min(closest, root.val, key=lambda x: (abs(target - x), x))
            root = root.left if root.val > target else root.right
        return closest

    def closest_tree_value_v1(self, root: Optional[TreeNode], target: int) -> float:
        """
        Approach: Inorder Iterative Approach
        T: O(K) Worst: O(H + K)
        S: O(H)
        :param root:
        :param target:
        :return:
        """
        stack = []
        prev = float("-inf")
        while root or stack:
            # perform inorder
            while root:
                # append stack
                stack.append(root)
                root = root.left
            root = stack.pop()
            # check the min value
            if prev <= target <= root.val:
                return min(prev, root.val, key=lambda x: abs(target - x))
            # assign the val to prev and move right
            prev = root.val
            root = root.right
        return prev

    def closest_tree_value_v0(self, root: Optional[TreeNode], target: int) -> int:
        """
        Approach: Recursion Inorder Traversal
        T: O(N)
        S: O(N)
        :param root:
        :param target:
        :return:
        """
        def inorder(node: TreeNode):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return min(inorder(root), key=lambda x: abs(target - x))