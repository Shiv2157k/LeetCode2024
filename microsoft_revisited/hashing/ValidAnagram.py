class Anagrams:

    def is_anagram(self, s: str, t: str) -> bool:
        """
        Approach: Hash Bucket
        T: O(N + M)
        S: O(1) -> 26 is a constant space
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False

        freq_bucket = [0] * 26

        for char in s:
            hash_key = ord(char) - ord('a')
            freq_bucket[hash_key] += 1

        for char in t:
            hash_key = ord(char) - ord('a')
            freq_bucket[hash_key] -= 1
            if freq_bucket[hash_key] < 0:
                return False
        return True
