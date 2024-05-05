from typing import List, Optional
from random import randint


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class ArrayToBST:

    def convert_v2(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Recursion with random left or right mid
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def to_bst(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            pivot = left + (right - left) // 2
            if left + right % 2 == 1:
                pivot += randint(0, 1)

            root = TreeNode(nums[pivot])
            root.left = to_bst(left, pivot - 1)
            root.right = to_bst(pivot + 1, right)
            return root

        return to_bst(0, len(nums) - 1)

    def convert_v1(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Recursion Right mid as node
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def to_bst(left: int, right: int) -> Optional[TreeNode]:

            if left > right:
                return None

            pivot = left + (right - left) // 2

            if left + right % 2 == 1:
                pivot += 1

            root = TreeNode(nums[pivot])
            root.left = to_bst(left, pivot - 1)
            root.right = to_bst(pivot + 1, right)
            return root

        return to_bst(0, len(nums) - 1)

    def convert_v0(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach: Recursion - choose left mid as node
        T: O(N)
        S: O(log N)
        :param nums:
        :return:
        """

        def to_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            pivot = left + (right - left) // 2

            root = TreeNode(nums[pivot])
            root.left = to_bst(0, pivot - 1)
            root.right = to_bst(pivot + 1, right)
            return root

        return to_bst(0, len(nums) - 1)
