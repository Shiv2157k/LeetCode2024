from typing import Optional, Tuple
from math import inf
from enum import Enum, auto


class Camera(Enum):
    HAS_CAMERA = auto()
    COVERED = auto()
    PLEASE_COVER = auto()


class TreeNode:

    def __init__(self, val: int = - 1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def min_camera_cover(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion / DFS
        T: O(N)
        S: O(H)

        :param root:
        :return:
        """
        camera = 0

        def cover(node: Optional[TreeNode]):
            nonlocal camera
            if not node:
                return Camera.COVERED

            left = cover(node.left)
            right = cover(node.right)

            if left == Camera.PLEASE_COVER or right == Camera.PLEASE_COVER:
                camera += 1
                return Camera.HAS_CAMERA

            if left == Camera.HAS_CAMERA or right == Camera.HAS_CAMERA:
                return Camera.COVERED
            return Camera.PLEASE_COVER

        return camera + 1 if cover(root) == Camera.PLEASE_COVER else camera

    def min_camera_cover_v1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        ans = 0
        covered = {None}

        def dfs(node, parent=None):
            nonlocal ans
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if parent is None and node not in covered or node.left not in covered or node.right not in covered:
                    ans += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)
        return ans

    def min_camera_cover_v0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        # case 0: strict subtree: All nodes below this are covered, but not this one
        # case 1: normal subtree: All nodes below and including this are covered - no camera
        # case 2: placed camera: All nodes below this are covered, plus camera is here

        def solve(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            if not node:
                return 0, 0, inf

            left = solve(node.left)
            right = solve(node.right)

            case_0 = left[1] + right[1]
            case_1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            case_2 = 1 + min(left) + min(right)

            return case_0, case_1, case_2

        return min(solve(root)[1:])
