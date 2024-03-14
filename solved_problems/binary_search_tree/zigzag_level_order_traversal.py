from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def zigzag_level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        result = []

        def dfs(node: TreeNode, level: int):

            if level >= len(result):
                result.append(deque[node.val])
            elif level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level + 1)
        dfs(root, 0)
        return result

    def zigzag_level_order_traversal_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        # validation
        if root is None:
            return []

        # results to store
        results = []
        level_list = deque()
        is_order_left = True

        # added None as a delimiter
        node_queue = deque([root, None])

        while node_queue:

            curr_node = node_queue.popleft()

            if curr_node:  # still on the same level
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:  # we have reached a new level
                # add the results
                results.append(level_list)
                # set the delimiter
                if len(node_queue) > 0:
                    node_queue.append(None)
                # clean-up level list and bool
                level_list = deque()
                is_order_left = not is_order_left
        return results

