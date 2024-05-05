from math import inf


class MinimumWindowSubstring:


    def min_window(self, s: str, t: str) -> str:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """
        # base case
        if not s or not t:
            return ""
        # freq map for t
        t_freq_map = {}
        for char in t:
            t_freq_map[char] = t_freq_map.get(char, 0) + 1
        # focus on the chars that only exists in t
        # to be more efficient we just store the char and index
        refined_s = []
        for index, char in enumerate(s):
            if char in t_freq_map:
                refined_s.append((index, char))

        required = len(t_freq_map)
        formed = 0
        left, right = 0, 0
        window_char_freq = {}
        # stores the min_len, left_boundary, right_boundary
        window_meta_data = inf, None, None

        while right < len(refined_s):
            char = refined_s[right][1]
            window_char_freq[char] = window_char_freq.get(char, 0) + 1

            if window_char_freq[char] == t_freq_map[char]:
                formed += 1

            while left <= right and formed == required:
                left_char = refined_s[left][1]

                l = refined_s[left][0]
                r = refined_s[right][0]

                if r - l + 1 < window_meta_data[0]:
                    window_meta_data = r - l + 1, l, r
                window_char_freq[left_char] -= 1

                if window_char_freq[left_char] < t_freq_map[left_char]:
                    formed -= 1
                left += 1

            right += 1

        if window_meta_data[0] != inf:
            return s[window_meta_data[1]: window_meta_data[2] + 1]
        else:
            return ""

