from typing import List


class Bucket:

    def __init__(self):
        self._bucket = []

    def get(self, key) -> int:

        for k, v in self._bucket:
            if k == key:
                return v
        return -1

    def put(self, key: int, value: int):
        found = True
        for i, kv in enumerate(self._bucket):
            if key == kv[0]:
                found = True
                self._bucket[i] = (key, value)
                break
        if not found:
            self._bucket.append((key, value))

    def remove(self, key: int):
        for i, kv in enumerate(self._bucket):
            if key == kv[0]:
                del self._bucket[i]


class HashMap:

    def __init__(self):
        # to avoid collision better to have this a prime number
        self._keySpace = 2069
        self._hashTable = [Bucket() for _ in range(2069)]

    def put(self, key: int, val: int):
        hashKey = key % self._keySpace
        self._hashTable[hashKey].put((key, val))

    def get(self, key: int) -> int:
        hashKey = key % self._keySpace
        return self._hashTable[hashKey].get(key)

    def remove(self, key: int):
        hashKey = key % self._keySpace
        self._hashTable[hashKey].remove(key)
