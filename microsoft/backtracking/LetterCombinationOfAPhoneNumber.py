from typing import List


class PhoneNumber:
    letterMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Approach: Back Track
        T: O(4^n * N)
        S: O(N)
        :param digits:
        :return:
        """

        if not digits:
            return []

        result = []

        def backtrack(pos: int, path: List[str]):

            if len(path) == len(digits):
                result.append("".join(path))
                return

            letters = self.letterMap.get(digits[pos])

            for letter in letters:
                path.append(letter)
                backtrack(pos + 1, path)
                path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    phoneNumber = PhoneNumber()
    print(phoneNumber.letterCombinations("23"))
