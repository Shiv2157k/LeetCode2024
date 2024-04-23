from typing import List


class Queue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        self._top = None

    def push(self, x: int):
        if not self._stack1:
            self._top = x
        self._stack1.append(x)

    def pop(self) -> int:
        if not self._stack2:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
        return self._stack2.pop()

    def peek(self) -> int:
        if self._stack2:
            return self._stack2[-1]
        return self._top

    def empty(self) -> bool:
        return not self._stack2 and not self._stack1
