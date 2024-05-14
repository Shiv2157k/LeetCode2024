from typing import Optional, List, Dict, Tuple


class TreeNode:

    def __ini__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def find_duplicates(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Approach: Optimized Triplet Map
        T: O(N)
        S: O(N)
        :param root: 
        :return:
        """

        def traverse(node: Optional[TreeNode]) -> int:

            if not node:
                return 0

            triplet = (traverse(node.left), node.val, traverse(node.right))

            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1

            curr_id = triplet_to_id[triplet]
            freq_map[curr_id] = freq_map.get(curr_id, 0) + 1

            if freq_map[curr_id] == 2:
                output.append(node)
            return curr_id

        triplet_to_id: Dict[Tuple[int, int, int], int] = {}
        freq_map: Dict[int, int] = {}
        output: List[TreeNode] = []
        traverse(root)
        return output
