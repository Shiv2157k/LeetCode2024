from typing import List


class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key: int) -> int:

        for k, v in self.bucket:
            if key == k:
                return v
        return -1

    def put(self, key: int, val: int) -> None:

        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i][key] = val
                found = True
                break
        if not found:
            self.bucket.append((key, val))

    def remove(self, key: int) -> None:

        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class HashMap:

    def __init__(self):
        # for less collision better to be a prime number
        self.key_space: int = 2069
        self.hashtable: List[Bucket] = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, val: int) -> None:
        hash_key = key % self.key_space
        self.hashtable[hash_key].put(key, val)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hashtable[hash_key].get(key)

    def remove(self, key: int):
        hash_key = key % self.key_space
        self.hashtable[hash_key].remove(key)
