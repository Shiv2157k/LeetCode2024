from typing import List


class TwoDimensionVector:

    def __init__(self, v: List[List[int]]):
        self._vector = v
        self._outer = 0
        self._inner = 0

    def _advance_to_next(self):
        while self._outer < len(self._vector) and self._inner == len(self._vector[self._outer]):
            self._outer += 1
            self._inner = 0

    def next(self):
        self._advance_to_next()
        result = self._vector[self._outer][self._inner]
        self._inner += 1
        return result

    def hashNext(self):
        self._advance_to_next()
        return self._outer < len(self._vector)


if __name__ == "__main__":

    two_d_vector = TwoDimensionVector(
        [
            [1, 2, 3], [], [], [5, 7, 9], [], [11]
        ]
    )
    print(two_d_vector.next())
    print(two_d_vector.next())
    print(two_d_vector.next())
    print(two_d_vector.next())
    print(two_d_vector.hashNext())
    print(two_d_vector.next())
    print(two_d_vector.next())
    print(two_d_vector.next())
    print(two_d_vector.hashNext())