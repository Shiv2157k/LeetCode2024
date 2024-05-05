from typing import List


class Anagrams:


    def find_all_anagrams(self, s: str, p: str) -> List[int]:
        """
        Approach: Hash
        T: O(S + P)
        S: O(1) -> O(26) constant
        :param s:
        :param p:
        :return:
        """

        if len(s) < len(p):
            return []

        s_len: int = len(s)
        p_len: int = len(s)

        p_freq_bucket: List[int] = [0] * 26
        s_freq_bucket: List[int] = [0] * 26

        for char in p:
            p_freq_bucket[ord(char) - ord('a')] += 1

        anagram_indices: List[int] = []

        right: int = 0
        while right < s_len:

            s_freq_bucket[ord(s[right]) - ord('a')] += 1

            if right >= p_len:
                s_freq_bucket[ord(s[right - p_len]) - ord('a')] -= 1

            if s_freq_bucket == p_freq_bucket:
                anagram_indices.append(right - p_len + 1)

            right += 1
        return anagram_indices

