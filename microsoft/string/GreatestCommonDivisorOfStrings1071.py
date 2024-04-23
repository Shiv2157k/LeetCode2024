class GreatestCommonDivisor:

    def ofStrings(self, s1: str, s2: str) -> str:
        """
        Approach: Greedy
        T: O(min(n1, n2) + (n1 + n2))
        S: O(1)
        :param s1:
        :param s2:
        :return:
        """

        n1, n2 = len(s1), len(s2)

        def isDivisor(size: int) -> bool:
            # validation or edge case
            if n1 % size or n2 % size:
                return False
            factor1, factor2 = n1 // size, n2 // size
            return s1[:size] * factor1 == s1 and s1[:size] * factor2 == s2

        for length in range(min(n1, n2), 0, -1):
            # greedily check from back
            if isDivisor(length):
                return s1[: length]
        return ""
