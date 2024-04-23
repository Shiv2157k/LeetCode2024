from typing import List


class PhoneNumber:

    def __init__(self):
        self.letterMap = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

    def getLetterCombinations(self, digits: str) -> List[str]:
        """
        Approach: Backtracking
        T: O(4^N * N)
        S: O(N)
        :param digits:
        :return:
        """
        # validation
        if not digits:
            return []

        def backtrack(pos: int, path: List[str]):

            # base case
            if len(path) == len(digits):
                letterCombinations.append("".join(path))
                return

            letters = self.letterMap.get(digits[pos])

            for letter in letters:
                path.append(letter)
                backtrack(pos + 1, path)
                path.pop()

        letterCombinations = []
        backtrack(0, [])
        return letterCombinations
