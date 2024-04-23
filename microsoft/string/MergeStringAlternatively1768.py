class MergeStrings:

    def alternatively(self, word1: str, word2: str) -> str:
        """
        Approach: Two Pointers
        T: O(N + M)
        S: O(1)
        :param word1:
        :param word2:
        :return:
        """

        n = max(len(word1), len(word2))

        result = []

        for i in range(n):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return "".join(result)
