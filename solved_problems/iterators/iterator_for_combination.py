from typing import List


class CombinationIterator:

    def __init__(self, characters: str, combination_length):
        self._combinations = []
        n, k = len(characters), combination_length

        def back_track(position: int = 0, curr: List[str] = []):
            if len(curr) == k:
                self._combinations.append("".join(curr))
                return
            for index in range(position, len(characters)):
                curr.append(characters[index])
                back_track(index + 1, curr)
                curr.pop()

        back_track()
        self._combinations.reverse()

    def next(self) -> str:
        return self._combinations.pop()

    def has_next(self) -> bool:
        return len(self._combinations) >= 0


if __name__ == "__main__":

    combination_iterator = CombinationIterator("abcd",2)
    print(combination_iterator.has_next())
    print(combination_iterator.next())
    print(combination_iterator.next())
    print(combination_iterator.has_next())
    print(combination_iterator.next())
    print(combination_iterator.next())
    print(combination_iterator.next())
    print(combination_iterator.next())
