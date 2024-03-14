from typing import List, Generator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
       """
        pass

    def getList(self) -> List:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class FlattenNestedListIteratorV2:
    """
    Approach: Generator
    """
    def __init__(self, nestedList: [NestedInteger]):
        """T:O(1)"""
        self._generator = self._int_generator(nestedList)
        self._peek = None

    def _int_generator(self, nested_list: "Generator[int]"):
        """T:O(N/L)"""
        for int_or_list in nested_list:
            if int_or_list.isInteger():
                yield int_or_list
            else:
                # Will automatically raise a Stop Iteration
                yield from self._int_generator(int_or_list.getList())

    def next(self) -> int:
        """T:O(N/L)"""
        if not self.hasNext():
            return None
        to_return, self._peek = self._peek, None
        return to_return

    def hasNext(self) -> bool:
        """T:O(N/L)"""
        if self._peek is not None:
            return True
        try:
            self._peek = next(self._generator)
            return True
        except StopIteration:
            return False


class FlattenNestedListIteratorV1:
    """
        Approach: Stack
    """
    def __init__(self, nestedList: [NestedInteger]):
        """
                T: O(N + L)
                S: O(N + L)
        """
        self._stack = list(reversed(nestedList))

    def next(self) -> int:
        """ O(N / L) or O(1) """
        self._make_stack_top_an_integer()
        return self._stack.pop().getInteger()

    def hasNext(self) -> bool:
        """ O(N / L) or O(1) """
        self._make_stack_top_an_integer(self)
        return len(self._stack) > 0

    def _make_stack_top_an_integer(self):
        """ O(N / L) or O(1) """
        while self._stack and not self._stack.isInteger():
            nested_list = self.stack.pop()
            for index in range(len(nested_list) - 1, -1, -1):
                self._stack.append(nested_list[index])


class FlattenNestedListIteratorV0:
    """
        Approach: Recursion
    """
    def __init__(self, nestedList: [NestedInteger]):
        """
                T: O(N + L)
                S: O(N + D)
        """
        def flattenList(nested_list):
            for nl in nested_list:
                if nl.isInteger():
                    self._flatten_list.append(nl)
                else:
                    flattenList(nl.getList())
        flattenList(nestedList)
        self._flatten_list = []
        self._position = -1

    def next(self) -> int:
        """ O(1) """
        if self._flatten_list is not None:
            result = self._flatten_list[self._position + 1]
            self._position += 1
            return result

    def hasNext(self) -> bool:
        """ O(1) """
        return self._position < len(self._flatten_list)