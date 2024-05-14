from typing import List


class Anagrams:

    def find_all_anagrams_in_string(self, s: str, p: str) -> List[int]:
        """
        Approach: Hash Bucket and Sliding Window
        T: O(N)
        S: O(1)
        :param s:
        :param p:
        :return:
        """

        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []

        p_freq_bucket = [0] * 26
        s_freq_bucket = [0] * 26

        for char in p:
            p_freq_bucket[ord(char) - ord('a')] += 1

        right = 0
        anagram_indices = []

        while right < s_len:

            s_freq_bucket[ord(s[right]) - ord('a')] += 1

            if right >= p_len:
                s_freq_bucket[ord(s[right - p_len]) - ord('a')] += 1

            if s_freq_bucket == p_freq_bucket:
                anagram_indices.append(right - p_len + 1)
            right += 1
        return anagram_indices

