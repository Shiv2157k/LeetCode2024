from typing import List, Tuple


class MinStack:
    """
    Approach: Using two stacks
    T: O(1) for all operations
    S: O(N)
    """

    def __init__(self):
        self.__stack: List[int] = []
        self.__min_stack: List[List[int]] = []

    def push(self, val: int):

        if not self.__min_stack or self.__min_stack[-1][0] >= val:
            if self.__min_stack and self.__min_stack[-1][0] == val:
                self.__min_stack[-1][1] += 1
            else:
                self.__min_stack.append([val, 1])
        self.__stack.append(val)

    def pop(self):

        if self.__min_stack[-1][0] == self.__stack[-1]:
            self.__min_stack[-1][1] -= 1
        if self.__min_stack[-1][1] <= 0:
            self.__min_stack.pop()
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def get_min(self) -> int:
        return self.__min_stack[-1][0]
