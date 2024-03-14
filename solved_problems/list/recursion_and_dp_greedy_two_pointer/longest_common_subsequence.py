from functools import lru_cache
from pprint import pprint


class Texts:

    def __init__(self):
        self._memo = [[]]

    def longestCommonSubSequence_v1(self, text1: str, text2: str) -> int:
        """
        Recursion + memoization
        T: O()
        S: O()
        :param text1:
        :param text2:
        :return:
        """

        def solveMemo(pointer1: int, pointer2: int) -> int:
            # base case
            if pointer1 == len(text1) or pointer2 == len(text2):
                return 0

            if self._memo[pointer1][pointer2] != -1:
                return self._memo[pointer1][pointer2]

            # option 1
            option1 = solveMemo(pointer1 + 1, pointer2)
            firstTextOccurence = text2.find(text1[pointer1], pointer2)

            option2 = 0
            # option 2
            if firstTextOccurence != -1:
                option2 = 1 + solveMemo(pointer1 + 1, firstTextOccurence + 1)
            self._memo[pointer1][pointer2] = max(option1, option2)
            return self._memo[pointer1][pointer2]

        self._memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return solveMemo(0, 0)

    def longestCommonSubSequence_v2(self, text1: str, text2: str) -> int:
        """
        Recursion + memoization + variation
        :param text1:
        :param text2:
        :return:
        """
        def solveMemo(pointer1: int, pointer2: int) -> int:

            # base case
            if pointer1 == len(text1) or pointer2 == len(text2):
                return 0
            if self._memo[pointer1][pointer2] != -1:
                return self._memo[pointer1][pointer2]

            # option1
            if text1[pointer1] == text2[pointer2]:
                self._memo[pointer1][pointer2] = 1 + solveMemo(pointer1 + 1, pointer2 + 1)
            else:
                self._memo[pointer1][pointer2] = max(solveMemo(pointer1 + 1, pointer2), solveMemo(pointer1, pointer2 + 1))
            return self._memo[pointer1][pointer2]

        self._memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return solveMemo(0, 0)

    def longestCommonSubSequence_v3(self, text1: str, text2: str) -> int:
        """
        Recursion with lru cache memoization
        :param text1:
        :param text2:
        :return:
        """
        @lru_cache(maxsize=None)
        def solveMemo(pointer1: int, pointer2: int) -> int:

            #base case
            if pointer1 == len(text1) or pointer2 == len(text2):
                return 0

            if text1[pointer1] == text2[pointer2]:
                return 1 + solveMemo(pointer1 + 1, pointer2 + 1)
            else:
                return max(solveMemo(pointer1, pointer2 + 1), solveMemo(pointer1 + 1, pointer2))
        return solveMemo(0, 0)

    def longestCommonSubSequence_v4(self, text1: str, text2: str) -> int:
        """
        DP
        T: O(MN)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # if the char is same
                if text1[row] == text2[col]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # otherwise
                else:
                    dp_grid[row][col] = max(dp_grid[row][col + 1], dp_grid[row + 1][col])
        return dp_grid[0][0]


    def longestCommonSubSequence_v5(self, text1: str, text2: str) -> int:
        """
        Optimized DP
        :param text1:
        :param text2:
        :return:
        """
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):

                if text1[row] == text2[col]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
                current, previous = previous, current
        return previous[0]


if __name__ == "__main__":

    texts = Texts()
    print(texts.longestCommonSubSequence_v5("abcde", "ace"))
    print(texts.longestCommonSubSequence_v4("abcde", "ace"))
    print(texts.longestCommonSubSequence_v3("abcde", "ace"))
    print(texts.longestCommonSubSequence_v2("abcde", "ace"))
    print(texts.longestCommonSubSequence_v1("abcde", "ace"))
    print("--------------*---------------")
    pprint([[[0] * 10 for _ in range(10)] for _ in range(5)])



