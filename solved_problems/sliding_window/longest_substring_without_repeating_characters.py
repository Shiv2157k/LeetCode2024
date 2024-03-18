class Substring:

    def longest_without_repeating_v2(self, s: str) -> int:
        """
        Sliding Window Optimized
        T: O(N)
        S: O(min(m, n))
        :param s:
        :return:
        """

        n = len(s)
        prev_occurrence = {}
        left = right = max_len = 0

        while right < n:
            char = s[right]
            if char in prev_occurrence:
                left = max(left, prev_occurrence[char])
            prev_occurrence[char] = right + 1
            right += 1
            max_len = max(max_len, right - left)
        return max_len

    def longest_without_repeating_v1(self, s: str) -> int:
        """
        Sliding window
        T: O(2N) -> O(N)
        S: O(min(m, n))
        :param s:
        :return:
        """
        n = len(s)
        freq_char = {}
        left = right = max_len = 0

        while right < n:
            right_char = s[right]
            freq_char[right_char] = freq_char.get(right_char, 0) + 1

            if freq_char[right_char] > 1:
                left_char = s[left]
                freq_char[left_char] -= 1
                left += 1
            right += 1
            max_len = max(max_len, right - left)
        return max_len

    def longest_without_repeating_v0(self, s: str) -> int:
        """
        Brute Force
        T: O(N^3)
        S: O(N)
        :param s:
        :return:
        """

        def is_not_duplicates(left: int, right: int) -> bool:
            visited = set()
            while left <= right:
                char = s[left]
                if char in visited:
                    return False
                visited.add(char)
                left += 1
            return True

        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_not_duplicates(i, j):
                    max_len = max(max_len, j - i + 1)
        return max_len


if __name__ == "__main__":
    substring = Substring()
    print(substring.longest_without_repeating_v0("abcded"))
    print(substring.longest_without_repeating_v0("abcdefgas"))
    print("___**___")
    print(substring.longest_without_repeating_v1("abcded"))
    print(substring.longest_without_repeating_v1("abcdefgas"))
    print("___**___")
    print(substring.longest_without_repeating_v2("abcded"))
    print(substring.longest_without_repeating_v2("abcdefgas"))
