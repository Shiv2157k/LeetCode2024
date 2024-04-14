from typing import Optional, List
from random import randint


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SortedArrayToBST:

    def convertV0(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            pivot = left + (right - left) // 2

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)

        return helper(0, len(nums) - 1)

    def convertV1(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search with right mid
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            pivot, odd = left + (right - left) // 2, (left + right) % 2

            if odd:
                pivot += 1

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root

        return helper(0, len(nums) - 1)

    def convertV2(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Binary Search with random left/ right mid
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            pivot, odd = left + (right - left) // 2, (left + right) % 2
            if odd:
                pivot += randint(0, 1)

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)

        return helper(0, len(nums) - 1)
