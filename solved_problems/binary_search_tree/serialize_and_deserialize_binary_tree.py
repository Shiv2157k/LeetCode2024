from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:

        def rserialize(root: Optional[TreeNode], string: str) -> str:
            if not root:
                string += "None"
            else:
                root_val = root.val
                string += str(root_val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, "")

    def deserialize(self, data: str) -> Optional[TreeNode]:

        def rdeserialize(string: List[str]) -> Optional[TreeNode]:
            if string[0] == "None":
                string.pop(0)
                return None
            root = TreeNode(int(string[0]))
            string.pop(0)
            root.left = rdeserialize(string)
            root.right = rdeserialize(string)
            return root

        data = data.split(",")
        return rdeserialize(data)
