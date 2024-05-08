from typing import List


class LetterCombinationOfPhoneNumber:

    def __init__(self):
        self._letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def get_all_combinations(self, digits: str) -> List[str]:
        """
        Approach: BackTrack
        T: O(4^N * N)
        S: O(N)
        :param digits:
        :return:
        """

        def backtrack(pos: int, path: List[str]) -> None:

            if len(path) == len(digits):
                combinations.append(''.join(path))
                return

            letters = self._letter_map.get(digits[pos])

            for letter in letters:
                path.append(letter)
                backtrack(pos + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
