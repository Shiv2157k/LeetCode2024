from typing import List


class PalindromicPartition:


    def partitionV1(self, s: str) -> List[List[str]]:
        """
        Approach: DP + Backtrack
        T: O(N * 2 ^ N)
        S: : O(N)
        :param s:
        :return:
        """
        results = []
        size = len(s)

        dp = [[False] * size for _ in range(size)]

        def backtrack(start: int, path: List[str]) -> None:

            if start >= len(s):
                results.append(path[:])

            for end in range(start, len(s)):

                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    path.append(s[start: end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return results

    def partitionV0(self, s: str) -> List[List[str]]:
        """
        Approach: Backtrack
        T: O(N * 2 ^ N)
        S: O(N)
        :param s:
        :return:
        """
        results = []

        def backtrack(start: int, path: List[str]) -> None:

            if start >= len(s):
                results.append(path[:])

            for end in range(start, len(s)):

                if self._isPalindrome(s, start, end):
                    path.append(s[start: end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        backtrack(0, [])
        return results

    def _isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    palindromicPartition = PalindromicPartition()
    print(palindromicPartition.partitionV0("aab"))
    print(palindromicPartition.partitionV0("kayak"))
    print("*******************")
    print(palindromicPartition.partitionV1("aab"))
    print(palindromicPartition.partitionV1("kayak"))
