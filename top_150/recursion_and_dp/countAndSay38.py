class Integer:

    def countAndSayV1(self, n: int) -> str:
        """
        Approach: Iterative
        T: O(E(n, k=1) L (K)) length of sequence for term k
        S: O(M) - max sequence up to n
        :param n:
        :return:
        """
        s = ["1"]

        for i in range(1, n):
            temp = []
            m, count = len(s), 1
            for j in range(1, m + 1):
                if j == m or s[j] != s[j - 1]:
                    temp.append(str(count))
                    temp.append(s[j - 1])
                    count = 0
                count += 1
            s = temp
        return "".join(s)

    def countAndSayV0(self, n: int) -> str:
        """
        Approach: Recursion
        T: O(E(n, k=1) L (K)) length of sequence for term k
        S: O(M) - max sequence up to n
        :param n:
        :return:
        """

        # base case
        if n == 1:
            return "1"

        s = self.countAndSayV0(n - 1)

        sLen = len(s)
        count = 1
        result = []

        for index in range(1, sLen + 1):

            if index == sLen or s[index] != s[index - 1]:
                result.append(str(count) + s[index - 1])
                count = 0
            count += 1
        return "".join(result)


if __name__ == "__main__":
    integer = Integer()
    print(integer.countAndSayV1(4))
    print(integer.countAndSayV1(3))
    print(integer.countAndSayV1(5))
    print("***(^)***")
    print(integer.countAndSayV0(4))
    print(integer.countAndSayV0(3))
    print(integer.countAndSayV0(5))
