class CountAndSay:

    def count_and_say_v1(self, n: int) -> str:
        """
        Approach: DP
        T: O(2 ^ N)
        S: O(N)
        :param n:
        :return:
        """

        s = ['1']

        for i in range(1, n):
            count = 1
            m = len(s)
            temp = []
            for j in range(1, m + 1):

                if j == m or s[j] != s[j - 1]:
                    temp.append(str(count))
                    temp.append(s[j - 1])
                    count = 0
                count += 1
            s = temp
        return ''.join(s)

    def count_and_say_v0(self, n: int) -> str:
        """
        Approach: Recursion
        T: O(2 ^ N)
        S: O(N)
        :param n:
        :return:
        """
        if n == 1:
            return '1'

        s = self.count_and_say_v0(n - 1)
        s_len = len(s)
        count = 1
        result = []

        for i in range(1, s_len + 1):
            if i == s_len or s[i] != s[i - 1]:
                result.append(str(count) + s[i - 1])
                count = 0
            count += 1
        return ''.join(result)
