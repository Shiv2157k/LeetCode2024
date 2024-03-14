"""
    Intuition
    To create a 5 digit palindrome we do not need to care about the middle element.
    We just need to find subsequence of pattern XY_YX.
    Calculate number of subsequences of type XY and subsequences of type YX around any given point i and
    multiply them to find number of subsequences of type XY_YX.
    Since string only has digits, the time complexity will be 100*n.

    Approach
    We will be maintaining the counts of digit in the list cnts
    Keep 2 arrays pre and suf to store the number of prefixes of type XY and suffixes of type YX. pre[i-1][1][2] means prefixes of type 12 before index i. Similarly suf[i+1][1][2] means suffixes of type 21 after index i
    Remember given string is made of digits that is 0123456789. That's a total of 10 unique characters
    Once we have calculated the prefix and suffix lists we just need to multiply pre[i - 1][j][k] with suf[i + 1][j][k] to find number of palindromic subsequences
        for (int i = 0; i < n; i++) {
            int c = s[i] - '0';
            if (i) {
                for (int j = 0; j < 10; j++)
                    for (int k = 0; k < 10; k++) {
                        pre[i][j][k] = pre[i - 1][j][k];
                        if (k == c) pre[i][j][k] += cnts[j];
                    }
            }
            cnts[c]++;
        }
    Explanation of above code:
    Use if (i) to not step outside of array limits when accessing pre[i-1]
    Let's say j = 5, k = 4 and c = 4 which means we are looking at prefix 54. pre[i][j][k] = pre[i - 1][j][k] will carry forward previous count of prefixes. Since k == c means the current character(s[i]) matches with last digit of prefix. To find total number of possibilites of prefixes of type 54 we need to know how many 5 exist before current index.
    This information is stored in cnts[5]. So we add cnts[5] to pre[i][5][4].
"""
from typing import List


class PalindromeSubsequence:

    def totalCountOfLengthFive(self, s: str) -> int:
        """
        Time complexity: O(N * 100) -> O(N)
        Space Complexity: O(N)
        Prefix and Suffix: 100 combination each * length
        Freq Counter: 0 - 9
        :param s:
        :return:
        """
        mod = 10 ** 9 + 7
        length = len(s)

        def findPrefixCount(s: str) -> List[List[List[int]]]:
            digitFreq = [0] * 10
            dp = [[[0] * 10 for _ in range(10)] for _ in range(length)]

            for index in range(length):
                digit = ord(s[index]) - ord('0')
                if index - 1 >= 0:
                    for pp in range(10):
                        for p in range(10):
                            dp[index][pp][p] = dp[index - 1][pp][p]
                            if digit == p: # found new prefix
                                # add it into our dp
                                dp[index][pp][p] += digitFreq[pp]
                digitFreq[digit] += 1
            return dp

        result = 0
        prefix = findPrefixCount(s)
        # as we want to find prefix xy of suffix yx need to reverse the string
        suffix = findPrefixCount(s[::-1])[::-1]
        for index in range(2, length -2):
            for pp in range(10):
                for p in range(10):
                    result += prefix[index - 1][pp][p] * suffix[index + 1][pp][p]
        return result % mod


if __name__ == "__main__":

    palSub = PalindromeSubsequence()
    print(palSub.totalCountOfLengthFive("103301"))