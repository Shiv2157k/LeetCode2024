from collections import deque
from typing import List


class PhoneNumber:
    letterMap = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }

    def generateLetterCombinationV1(self, digits: str) -> List[str]:
        """
        Approach: Back Tracking
        T: O(4 ^ N * N)
        S: O(N)
        :param digits:
        :return:
        """
        if not digits:
            return []

        combinations = []

        def backtrack(position: int, path: List[str]):

            # base case
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # backtrack

            letters = self.letterMap[digits[position]]

            for letter in letters:
                path.append(letter)
                backtrack(position + 1, path)
                path.pop()

        backtrack(0, [])
        return combinations

    def generateLetterCombinationV0(self, digits: str) -> List[str]:
        """
        Approach: Using Queue (BFS)
        T: O(4^N * N)
        S: O(4^N)
        :param digits:
        :return:
        """

        if not digits:
            return []

        queue = deque(self.letterMap[digits[0]])

        for index in range(1, len(digits)):
            size = len(queue)
            for _ in range(size):
                path = queue.popleft()

                for letter in self.letterMap[digits[index]]:
                    queue.append(path + letter)
        return queue


if __name__ == "__main__":
    phoneNumber = PhoneNumber()
    print(phoneNumber.generateLetterCombinationV1("23"))
    print(phoneNumber.generateLetterCombinationV1("2"))
    print(phoneNumber.generateLetterCombinationV1("999"))

    print(phoneNumber.generateLetterCombinationV0("23"))
    print(phoneNumber.generateLetterCombinationV0("2"))
    print(phoneNumber.generateLetterCombinationV0("999"))
