

class MyQueue:
    """
    Amortized
    """
    def __init__(self):
        self._s1 = []
        self._s2 = []
        self._front = None

    def push(self, x: int):
        if not self._s1:
            self._front = x
        self._s1.append(x)

    def pop(self):
        if not self._s2:
            while self._s1:
                self._s2.append(self._s2.pop())
        return self._s2.pop()

    def peek(self):
        if self._s2:
            return self._s2[-1]
        return self._front

    def empty(self) -> bool:
        return not self._s1 and not self._s2

class Queue:

    def __init__(self):
        self._s1 = []
        self._s2 = []
        self._front = None

    def push(self, x: int):
        """
        -> Transfer from s1 to s2
        :param x:
        :return:
        """
        if not self._s1:
            self._front = x
        while self._s1:
            self._s2.append(self._s1.pop())
        self._s2.append(x)
        while self._s2:
            self._s1.append(self._s2.pop())

    def pop(self) -> int:
        res = self._s1.pop()
        if self._s1:
            self._front = self._s1[-1]
        return res

    def peek(self) -> int:
        return self._front

    def isEmpty(self):
        return not self._s1