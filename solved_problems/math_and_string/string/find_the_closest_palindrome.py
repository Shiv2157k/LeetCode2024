class ClosestPalindrome:

    def find(self, n: str) -> str:
        """
        Approach: Case Study
        Example 1: 1234 -> o/p: 1221
        Case 1: Extremes on both ends 999 --- 10001
        Case 2: 12 (first half)
        2.1 - first_half - 1 and reverse(first_half - 1) = 1111
        2.2 - first_half and reverse(first_half) = 1221
        2.3 - first_half + 1 and reverse(first_half + `) = 1331
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """
        size = len(n)

        prefix = int(n[: (size + 1) // 2])
        candidates = [str(10 ** (size - 1) - 1), str(10 ** size + 1)]
        result = ''

        # build candidates for case 2: 2.1, 2.2, 2.3
        for first_half in map(str, (prefix - 1, prefix, prefix + 1)):
            if size % 2 == 1:
                second_half = first_half[: -1]
            else:
                second_half = first_half
            candidates.append(first_half + second_half[::-1])

        for candidate in candidates:
            if (result == '' or
                    abs(int(n) - int(candidate)) < abs(int(n) - int(result)) or
                    (abs(int(n) - int(candidate)) == abs(int(n) - int(result)) and
                     int(candidate) < int(result))):
                result = candidate
        return result


if __name__ == "__main__":
    closest_pal = ClosestPalindrome()
    print(closest_pal.find("1234"))
    print(closest_pal.find("123"))
    print(closest_pal.find("10002"))
    print(closest_pal.find("10000"))
    print(closest_pal.find("12"))
    print(closest_pal.find("1"))
    print(closest_pal.find("9"))
    print(closest_pal.find("10"))
