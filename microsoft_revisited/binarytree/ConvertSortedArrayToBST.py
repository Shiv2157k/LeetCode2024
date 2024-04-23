from typing import Optional, List
from random import randint


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def sortedArrayToBSTV2(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(left, right):

            if left > right:
                return None

            pivot = left + (right - left) // 2

            if (left + right) % 2 == 1:
                pivot += randint(0, 1)

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root

        return helper(0, len(nums) - 1)

    def sortedArrayToBSTV1(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if left > right:
                return None

            pivot = left + (right - left) // 2
            if (left + right) % 2 == 1:
                pivot += 1

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root

        return helper(0, len(nums) - 1)

    def sortedArrayToBSTV0(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            pivot = left + (right - left) // 2

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root

        return helper(0, len(nums) - 1)
