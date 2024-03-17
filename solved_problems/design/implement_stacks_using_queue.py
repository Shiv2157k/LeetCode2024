from collections import deque


class StackV1:
    """
    Implementation with Single Queue
    """
    def __init__(self):
        self._q = deque()

    def push(self, x: int) -> None:
        self._q.append(x)
        size = len(self._q)
        while size > 1:
            self._q.append(self._q.popleft())
            size -= 1

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return len(self._q) == 0

class StackV0:
    """
    Implementation with Two Queues
    """
    def __init__(self):
        self._q1 = deque()
        self._q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self._top = x
        self._q1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        size = len(self._q1)
        while size > 1:
            self._top = self._q1.popleft()
            self._q2.append(self._top)
            size -= 1
        element = self._q1.pop()
        self._q1 = self._q2
        self._q2 = deque()
        return element

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self._q1) == 0 and len(self._q2) == 0


if __name__ == "__main__":
    stack_v0 = StackV0()
    print(stack_v0.push(9))
    print(stack_v0.push(8))
    print(stack_v0.push(7))
    print(stack_v0.top())
    print(stack_v0.pop())
    print(stack_v0.top())
    print(stack_v0.empty())

    print("***__***")
    stack_v1 = StackV1()
    print(stack_v1.push(9))
    print(stack_v1.push(8))
    print(stack_v1.push(7))
    print(stack_v1.top())
    print(stack_v1.pop())
    print(stack_v1.top())
    print(stack_v1.pop())
    print(stack_v1.top())
    print(stack_v1.empty())

