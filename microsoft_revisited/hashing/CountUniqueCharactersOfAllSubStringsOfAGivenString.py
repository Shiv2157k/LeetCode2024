from typing import List


class String:

    def count_unique_letter_string(self, s: str) -> int:
        """
        Approach: Hash Bucket
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        mod: int = 10 ** 7
        n: int = len(s)

        bucket = [[-1] for _ in range(26)]

        for i in range(n):
            bucket[ord(s[i]) - ord('A')].append(i)

        for i in range(len(bucket)):
            bucket[i].append(n)

        count = 0

        for i in range(len(bucket)):
            for j in range(1, len(bucket[i]) - 1):
                count += (bucket[i][j] - bucket[i][j - 1]) * (bucket[i][j + 1] - bucket[i][j])
        return count % mod
