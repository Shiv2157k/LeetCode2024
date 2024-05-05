from typing import List


class Strings:

    def merge_alternatively(self, word1: str, word2: str) -> str:
        """
        Approach: Linear
        T: O(max(m, n))
        S: O(N)
        :param word1:
        :param word2:
        :return:
        """

        n = max(len(word1), len(word2))
        output: List[str] = []

        for i in range(n):

            if i < len(word1):
                output.append(word1[i])
            if i < len(word2):
                output.append(word2[i])
        return "".join(output)
