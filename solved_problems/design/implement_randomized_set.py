from random import choice


class RandomizedSet:
    """
    For insert and delete
    T: O(1)
    - in worst case especially in java it will be O(N) due to list relocation
      when there is heavy data being appended
    S: O(N) - for hashmap and list
    """

    def __init__(self):
        self._cache = dict()
        self._list = []

    def insert(self, val: int) -> bool:
        # check if val in cache/ hashmap
        # exists return False
        if val in self._cache:
            return False
        # store the value in cache for reference
        # key: val/ element, value: index
        self._cache[val] = len(self._list)
        # append into the list helps with randomization
        # as the hashmap does not support.
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._cache:
            return False
        # to make this in O(1) we need to
        # swap the list and move the element to be remove
        # at the end of the list so that we can just pop
        # also we need to delete this key in the hashmap
        # and update the swapped element index uff...
        index, last_element = self._cache[val], self._list[-1]
        self._list[index], self._cache[last_element] = last_element, index

        self._list.pop()
        del self._cache[val]
        return True

    def random(self) -> int:
        """
        T: O(1)
        :return:
        """
        return choice(self._list)


if __name__ == "__main__":
    randomized_set = RandomizedSet()
    print(randomized_set.insert(2))
    print(randomized_set.insert(3))
    print(randomized_set.insert(9))
    print(randomized_set.insert(7))
    print(randomized_set.random())
    print(randomized_set.random())
    print(randomized_set.remove(9))
    print(randomized_set.remove(5))
    print(randomized_set.insert(2))