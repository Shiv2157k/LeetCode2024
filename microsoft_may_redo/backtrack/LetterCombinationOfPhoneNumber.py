from typing import List


class PhoneNumber:

    def letter_combinations(self, digits: str) -> List[str]:
        """
        Approach: Backtrack
        T: O(4^N * N)
        S: O(N)
        :param digits:
        :return:
        """

        phone_number_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(pos: int, path: List[str]) -> None:

            if len(path) == len(digits):
                combinations.append(''.join(path))
                return

            letters = phone_number_map.get(digits[pos])

            for letter in letters:
                path.append(letter)
                backtrack(pos + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
