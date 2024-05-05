from typing import Optional, List

class TreeNode:


    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        """
        Approach: BackTrack
        T: O(N^2) -> Worst Case
        S: O(N)
        :param root:
        :return:
        """
        path_lists = []
        self._back_track(root, target_sum, [], path_lists)
        return path_lists


    def _back_track(self, node: Optional[TreeNode], target: int, path: List[int], path_lists: List[List[int]]):

        if not node:
            return # backtrack

        path.append(node.val)

        if not node.left and not node.right and target == node.val:
            path_lists.append(list(path))
        else:
            self._back_track(node.left, target - node.val, path, path_lists)
            self._back_track(node.right, target - node.val, path, path_lists)
        path.pop()



