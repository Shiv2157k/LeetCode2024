from random import choice


class RandomizedSet:

    def __init__(self):
        self.__cache = {}
        self.__list = []

    def insert(self, val: int) -> bool:

        if val in self.__cache:
            return False
        self.__cache[val] = len(self.__list)
        self.__list.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self.__cache:
            return False

        # this is tricky part
        curr_val_index, last_val = self.__cache[val], self.__list[-1]
        self.__cache[last_val], self.__list[curr_val_index] = curr_val_index, last_val

        self.__list.pop()
        del self.__cache[val]
        return True

    def get_random(self) -> int:
        return choice(self.__list)
