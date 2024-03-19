from typing import Optional


class BSTNode:

    def __init__(self, value: int=-1):
        self.val = value
        self.left = None
        self.right = None


class BSTIteratorII:

    def __init__(self, root: Optional[BSTNode]):
        self.node = root
        self.pointer = -1
        self.stack, self.arr = [], []

    def next(self):
        self.pointer += 1

        # pre computation is completed
        # need to reload
        if self.pointer == self.arr:
            while self.node:
                self.stack.append(self.node)
                self.node = self.node.left

            curr = self.stack.pop()
            self.node = curr.right
            self.arr.append(curr.val)
        return self.arr[self.pointer]

    def prev(self):
        self.pointer -= 1
        return self.arr[self.pointer]

    def hasNext(self):
        return self.stack or self.pointer < len(self.arr) - 1

    def hasPrev(self):
        return self.pointer > 0