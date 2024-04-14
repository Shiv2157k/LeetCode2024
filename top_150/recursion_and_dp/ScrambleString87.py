class ScrambledString:

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Approach: DP top down
        T: O(N^2)
        S: O(N^2)
        :param s1:
        :param s2:
        :return:
        """

        def recurseWithMemo(sub1: str, sub2: str) -> bool:

            # base case 1
            if len(sub1) == 1:
                return sub1[0] == sub2[0]

            # base case 2
            if sorted(sub1) != sorted(sub2):
                return False

            if (sub1, sub2) in memo:
                return memo[(sub1, sub2)]

            # initiate memo
            memo[(sub1, sub2)] = False

            n = len(sub1)
            for k in range(1, n):
                # case 1
                noSwap = recurseWithMemo(sub1[:k], sub2[:k]) and recurseWithMemo(sub1[k:], sub2[k:])
                # case 2
                swap = recurseWithMemo(sub1[:k], sub2[n - k:]) and recurseWithMemo(sub1[k:], sub2[:n - k])

                if swap or noSwap:
                    memo[(sub1, sub2)] = True
                    break
            return memo[(sub1, sub2)]

        memo = {}
        return recurseWithMemo(s1, s2)


if __name__ == "__main__":
    srambleString = ScrambledString()
    print(srambleString.isScramble("great", "rgeat"))
    print(srambleString.isScramble("abcde", "caebd"))

