class UniqueCharactersOfAllSubstrings:

    def count_from_string(self, s: str) -> int:
        """
        Approach: Hash Bucket indices as val
        T: O(N)
        S: O(1) -> constant space
        :param s:
        :return:
        """

        mod = 1000000007
        n = len(s)

        hash_bucket = [[] for _ in range(26)]

        # add left sentinel for all the buckets
        for i in range(26):
            hash_bucket[i].append(-1)

        # add indices of the char
        for index, char in enumerate(s):
            hash_bucket[ord(char) - ord('A')].append(index)

        # add right sentinel for all the buckets
        for i in range(26):
            hash_bucket[i].append(n)

        count = 0

        for i in range(26):
            for j in range(1, len(hash_bucket[i]) - 1):
                p1 = (hash_bucket[i][j] - hash_bucket[i][j - 1])
                p2 = (hash_bucket[i][j + 1] - hash_bucket[i][j])
                product = p1 * p2
                count += product
        return count % mod
