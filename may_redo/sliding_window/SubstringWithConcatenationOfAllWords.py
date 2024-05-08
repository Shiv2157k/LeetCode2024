from typing import List


class SubstringWithConcatenationOfAllWords:

    def find_sub_string_v1(self, s: str, words: List[str]) -> List[int]:
        """
        Approach: Sliding Window
        T: O(N^2)
        S: O(M + K)
        :param s:
        :param words:
        :return:
        """

        s_len = len(s)
        word_len = len(words[0])
        sub_str_len = len(words) * word_len

        if s_len < sub_str_len:
            return []

        words_freq = {}
        for word in words:
            words_freq[word] = words_freq.get(word, 0) + 1

        output = []
        word_count = len(words)

        for i in range(word_len):

            left = i
            seen = {}
            count = 0

            for j in range(i, s_len - word_count + 1, word_len):

                word = s[j: j + word_len]

                if word in words_freq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > words_freq[word]:
                        seen[s[left: left + word_len]] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        output.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len
        return output

    def find_sub_string_v0(self, s: str, words: List[str]) -> List[int]:
        """
        Approach: Sliding Window
        T: O(N * M * K)
        S: O(M + K)
        :param s:
        :param words:
        :return:
        """

        s_len = len(s)
        word_len = len(words[0])
        sub_str_len = len(words) * word_len

        # validation
        if s_len < sub_str_len:
            return []

        words_freq = {}
        for word in words:
            words_freq[word] = words_freq.get(word, 0) + 1

        left = 0
        output = []

        while left <= s_len - sub_str_len:
            word_seen = {}
            formed_words = 0
            right = left
            while right < s_len:

                if right + word_len > s_len:
                    break

                sub_str = s[right: right + word_len]
                word_seen[sub_str] = word_seen.get(sub_str, 0) + 1

                if sub_str not in words_freq or word_seen[sub_str] > words_freq[sub_str]:
                    break

                formed_words += word_len

                if formed_words == sub_str_len:
                    output.append(left)
                    break
                right += word_len
            left += 1
        return output