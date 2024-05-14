class SumOfBeautyOfAllSubstrings:

    def beauty_sum(self, s: str) -> int:
        """
        Approach: Freq Map with two pointers
        T: O(N^2)
        S: O(N)
        :param s:
        :return:
        """

        total_sum = 0
        left = 0

        while left < len(s):

            freq_map = {}
            freq_map[s[left]] = freq_map.get(s[left], 0) + 1
            max_freq = freq_map[s[left]]
            min_freq = freq_map[s[left]]

            right = left + 1

            while right < len(s):
                freq_map[s[right]] = freq_map.get(s[right], 0) + 1
                max_freq = max(max_freq, freq_map[s[right]])
                min_freq = min(freq_map.values())
                total_sum += max_freq - min_freq
                right += 1
            left += 1
        return total_sum
