class Strings:

    def merge_two_strings_alternatively(self, word1: str, word2: str) -> str:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param word1:
        :param word2:
        :return:
        """
        n = max(len(word1), len(word2))
        output = []

        for i in range(n):

            if i < len(word1):
                output.append(word1[i])
            if i < len(word2):
                output.append(word1[i])
        return ''.join(output)
