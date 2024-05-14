from typing import Optional
from enum import Enum


class TreeNode:

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class CameraState(Enum):
    COVERED = 0
    HAS_CAMERA = 1
    PLEASE_COVER = 2


class BinaryTree:

    def min_camera_cover_v1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Greedy + DFS
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        min_cameras = 0
        covered = {None}

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
            nonlocal min_cameras

            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if parent is None and node not in covered or node.left not in covered or node.right not in covered:
                    min_cameras += 1
                    covered.update({parent, node, node.left, node.right})

        dfs(root, None)
        return min_cameras

    def min_camera_cover_v0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        :param root:
        :return:
        """

        min_cameras = 0

        def solve(node: Optional[TreeNode]) -> CameraState:
            nonlocal min_cameras

            if not node:
                return CameraState.COVERED

            left = solve(node.left)
            right = solve(node.right)

            if left == CameraState.PLEASE_COVER or right == CameraState.PLEASE_COVER:
                min_cameras += 1
                return CameraState.HAS_CAMERA

            if left == CameraState.HAS_CAMERA or right == CameraState.HAS_CAMERA:
                return CameraState.COVERED
            return CameraState.PLEASE_COVER

        return min_cameras + 1 if CameraState.PLEASE_COVER == solve(root) else min_cameras
