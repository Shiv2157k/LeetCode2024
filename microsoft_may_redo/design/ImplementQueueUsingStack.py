class MyQueue:

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
        self.__top = None

    def push(self, x: int) -> None:
        if not self.__stack1:
            self.__top = x
        self.__stack1.append(x)

    def pop(self, x: int) -> int:

        if not self.__stack2:
            while self.__stack1:
                self.__stack2.append(self.__stack1.pop())
        return self.__stack2.pop()

    def peek(self) -> int:

        if self.__stack2:
            return self.__stack2[-1]
        return self.__top

    def empty(self):
        return not self.__stack1 and not self.__stack2
