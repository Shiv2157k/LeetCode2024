from random import choice


class RandomizedSet:

    def __init__(self):
        self._cache = []
        self._list = []

    def insert(self, val: int) -> bool:

        if val in self._cache:
            return False

        self._cache[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self._cache:
            return False

        last_val, val_index = self._list[-1], self._cache[val]
        self._list[val_index], self._cache[last_val] = last_val, val_index
        self._list.pop()
        del self._cache[val]
        return True

    def getRandom(self) -> int:
        return choice(self._list)
