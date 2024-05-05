class ScrambleString:

    def is_scramble(self, s1: str, s2: str) -> bool:
        """
        Approach: Recurse with memo
        T: O()
        S: O()
        :param s1:
        :param s2:
        :return:
        """

        def dfs(sub1: str, sub2: str):

            if len(sub1) == 1:
                return sub1[0] == sub2[0]

            if sorted(sub1) != sorted(sub2):
                return False

            if (sub1, sub2) in memo:
                return memo[(sub1, sub2)]

            memo[(sub1, sub2)] = False
            n = len(sub1)

            for i in range(1, n):

                # case 1: no swap
                no_swap = dfs(sub1[:i], sub2[:i]) and dfs(sub1[i:], sub2[i:])

                # case2: swap
                swap = dfs(sub1[:i], sub2[n - i:]) and dfs(sub1[i:], sub2[: n - i])

                if swap or no_swap:
                    memo[(sub1, sub2)] = True
                    break
            return memo[(sub1, sub2)]

        memo = {}
        return dfs(s1, s2)
