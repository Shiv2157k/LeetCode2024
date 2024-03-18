class Anagrams:

    def min_steps_to_transform(self, s: str, t: str) -> int:
        """
        Approach: Hash Table
        T: O(N)
        S: O(1)
        :param s:
        :param t:
        :return:
        """
        char_freq = [0] * 26
        for index in range(len(s)):
            char_freq[ord(t[index]) - ord('a')] += 1
            char_freq[ord(s[index]) - ord('a')] -= 1

        min_steps = 0

        for freq_diff in char_freq:
            min_steps += max(0, freq_diff)
        return min_steps


if __name__ == "__main__":
    anagrams = Anagrams()
    print(anagrams.min_steps_to_transform("leetcode", "practice"))
    print(anagrams.min_steps_to_transform("eat", "tea"))
    print(anagrams.min_steps_to_transform("abcde", "fghij"))
