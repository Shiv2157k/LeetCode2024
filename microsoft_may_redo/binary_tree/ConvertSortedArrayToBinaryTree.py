from typing import Optional, List
from random import randint


class TreeNode:

    def __init__(self, val: int=-1, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def convert_to_bst_v2(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search Recursion
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            pivot = left + (right - left) // 2
            if (left + right) % 2 == 1:
                pivot += randint(0, 1)

            root = TreeNode(nums[pivot])
            root.left = convert(left, pivot - 1)
            root.right = convert(pivot + 1, right)
            return root

        return convert(0, len(nums) - 1)

    def convert_to_bst_v1(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search Recursion
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            pivot = left + (right - left) // 2
            if (left + right) % 2 == 1:
                pivot += 1

            root = TreeNode(nums[pivot])
            root.left = convert(left, pivot - 1)
            root.right = convert(pivot + 1, right)
            return root
        return convert(0, len(nums) - 1)

    def convert_to_bst_v0(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search Recursion
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        def convert(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            pivot = left + (right - left) // 2
            node = TreeNode(nums[pivot])

            node.left =  convert(left, pivot - 1)
            node.right = convert(pivot + 1, right)
            return node
        return convert(0, len(nums) - 1)