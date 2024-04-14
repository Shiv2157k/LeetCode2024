class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key: int):

        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key: int, val: int):

        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                found = True
                self.bucket[i] = (key, val)
                break
        if not found:
            self.bucket.append((key, val))

    def remove(self, key: int):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class HashMap:

    def __init__(self):
        self.keySpace = 2069
        self.hashTable = [Bucket() for _ in range(self.keySpace)]

    def put(self, key: int, value: int):
        hashKey = key % self.keySpace
        self.hashTable[hashKey].update(key, value)

    def get(self, key: int) -> int:
        hashKey = key % self.keySpace
        return self.hashTable[hashKey].get(key)

    def remove(self, key: int) -> None:
        hashKey = key % self.keySpace
        self.hashTable[hashKey].remove(key)
