class Palindrome:

    def longest_palindromic_substring_v2(self, s: str) -> str:
        """
        Approach: Expand Center
        Observations:
        Here we are going to consider each character as a center and expand to
        figure out the longest palindrome
        We need to make sure to handle below edge cases
        For odd length:
        For expanding we consider just i -> i.e., i, i
        For even length:
        For expanding, we consider i and i + 1
        When there are two words say: aa
        mid will be 1 but there is no left - 1 and right + 1
        So, mid = (right - left ) // 2 + 1
        T: O(N^2)
        S: O(1)
        :param s:
        :return:
        """
        length = len(s)
        left_index = right_index = 0

        def expand_center(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for index in range(len(s)):
            odd_length = expand_center(index, index)
            if odd_length > right_index - left_index:
                mid = odd_length // 2
                left_index, right_index = index - mid, index + mid

            even_length = expand_center(index, index + 1)
            if even_length > right_index - left_index:
                mid = (even_length // 2) - 1
                left_index, right_index = index - mid, index + mid + 1
        return s[left_index: right_index + 1]

    def longest_palindromic_substring_v1(self, s: str) -> str:
        """
        Approach: DP
        T: O(N^2)
        S: O(N)
        :param s:
        :return:
        """
        if not s:
            return ''
        length = len(s)
        max_length = 1
        start = 1
        dp = [[False] * length for _ in range(length)]

        # marking odd palindrome with length 1
        for i in range(length):
            dp[i][i] = True

        # marking even palindrome with length 2
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        curr_length = 3
        while curr_length <= length:
            left = 0
            while left < length - curr_length + 1:
                # Get the ending index of
                # substring from starting
                # index i and length diff
                right = left + curr_length - 1
                if s[right] == s[left] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    if max_length < curr_length:
                        max_length = curr_length
                        start = left
                left += 1
            curr_length += 1
        return s[: max_length] if max_length == start else s[start: start + max_length]

    def longest_palindromic_substring_v0(self, s: str) -> str:
        """
        Approach:
        T: O(N^3)
        S: O(1)
        :param s:
        :return:
        """
        def check_pal(left: int, right: int) -> bool:
            right -= 1
            while 0 <= left < len(s) and 0 <= right < len(s):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        length = len(s)
        for curr_length in range(length, 0, -1):
            for start in range(length - curr_length + 1):
                if check_pal(start, start + curr_length):
                    return s[start: start + curr_length]


if __name__ == "__main__":
    palidrome = Palindrome()
    print(palidrome.longest_palindromic_substring_v0("racecar"))
    print(palidrome.longest_palindromic_substring_v0('a'))
    print(palidrome.longest_palindromic_substring_v0("aabb"))
    print(palidrome.longest_palindromic_substring_v0("abc"))
    print(palidrome.longest_palindromic_substring_v0("bb"))
    print("--_--")
    print(palidrome.longest_palindromic_substring_v1("racecar"))
    print(palidrome.longest_palindromic_substring_v1('a'))
    print(palidrome.longest_palindromic_substring_v1("aabb"))
    print(palidrome.longest_palindromic_substring_v1("abc"))
    print(palidrome.longest_palindromic_substring_v1("bb"))
    print("--_--")
    print(palidrome.longest_palindromic_substring_v2("racecar"))
    print(palidrome.longest_palindromic_substring_v2('a'))
    print(palidrome.longest_palindromic_substring_v2("aabb"))
    print(palidrome.longest_palindromic_substring_v2("abc"))
    print(palidrome.longest_palindromic_substring_v2("bb"))
    print("--_--")