class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        if not self._minStack or self._minStack[-1][0] >= val:
            if self._minStack and self._minStack[-1][0] == val:
                self._minStack[-1][1] += 1
            else:
                self._minStack.append([val, 1])
        self._stack.append(val)

    def pop(self) -> None:
        if self._stack[-1] == self._minStack[-1][0]:
            self._minStack[-1][1] -= 1
        if self._minStack[-1][1] <= 0:
            self._minStack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minStack[-1][0]
