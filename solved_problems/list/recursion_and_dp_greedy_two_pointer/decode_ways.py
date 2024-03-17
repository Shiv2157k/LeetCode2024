

class DecodeWays:

    def __init__(self):
        self._memo = {}

    def total_number_v2(self, s: str) -> int:
        """
        Approach: DP Optimized
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        if s[0] == "0":
            return 0
        size = len(s)
        if size == 1:
            return 1
        two_back = 1
        one_back = 1 if s[1] != "0" else 0

        for index in range(1, len(s)):
            current = 0
            if s[index] != "0":
                current += one_back
            two_digit = int(s[index - 1: index + 1])
            if 10 <= two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        return one_back

    def total_number_v1(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        if s[0] == "0":
            return 0
        size = len(s)
        if size == 1:
            return 1
        dp = [0] * (size + 1)
        dp[0] = 1
        dp[1] = 1 if s[1] != "0" else 0

        for index in range(1, len(s)):
            if s[index] != "0":
                dp[index + 1] += dp[index]
            two_digit = int(s[index - 1: index + 1])
            if 10 <= two_digit <= 26:
                dp[index + 1] += dp[index - 1]
        return dp[-1]

    def total_number_v0(self, s: str) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        self._memo = {}
        return self.recursion_with_memo(0, s)

    def recursion_with_memo(self, index: int, s: str) -> int:

        # base cases
        if index == len(s):
            return 1
        if s[index] == "0":
            return 0
        if index in self._memo:
            return self._memo[index]
        if index == len(s) - 1:
            return 1

        decode = self.recursion_with_memo(index + 1, s)
        if int(s[index:index + 2]) <= 26:
            decode += self.recursion_with_memo(index + 2, s)
        self._memo[index] = decode
        return decode


if __name__ == "__main__":
    decode_ways = DecodeWays()
    print(decode_ways.total_number_v0("123"))
    print(decode_ways.total_number_v0("023"))
    print(decode_ways.total_number_v0("223521"))
    print("____*____")
    print(decode_ways.total_number_v1("123"))
    print(decode_ways.total_number_v1("023"))
    print(decode_ways.total_number_v1("223521"))
    print("____*____")
    print(decode_ways.total_number_v2("123"))
    print(decode_ways.total_number_v2("023"))
    print(decode_ways.total_number_v2("223521"))
