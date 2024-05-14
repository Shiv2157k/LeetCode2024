class Bucket:

    def __init__(self):
        self.__bucket = []

    def get(self, key: int) -> int:

        for k, v in self.__bucket:
            if k == key:
                return v
        return -1

    def put(self, key: int, val: int) -> None:
        found = False
        for i, kv in self.__bucket:
            if kv[0] == key:
                self.__bucket[i] = (key, val)
                found = True
                break
        if not found:
            self.__bucket.append((key, val))

    def remove(self, key: int, val: int) -> None:

        for i, kv in self.__bucket:
            if kv[0] == key:
                del self.__bucket[i]


class HashMap:
    """
    Approach: Array + Modulo
    T: O(N / k) for each method
    S: O(K + M)
    """
    def __init__(self):
        self.__key_space = 2069  # largest prime number to avoid collision
        self.__hash_table = [Bucket() for _ in range(self.__key_space)]

    def get(self, key: int) -> int:
        hash_key = key % self.__key_space
        return self.__hash_table[hash_key].get(key)

    def put(self, key: int, val: int) -> None:
        hash_key = key % self.__key_space
        self.__hash_table[hash_key].put(key, val)

    def remove(self, key: int) -> None:
        hash_key = key % self.__key_space
        self.__hash_table[hash_key].remove(key)
