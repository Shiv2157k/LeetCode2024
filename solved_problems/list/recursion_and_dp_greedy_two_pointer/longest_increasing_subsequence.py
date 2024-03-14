from typing import List


class Subsequences:

    def longestIncreasingSequence(self, nums: List[int]) -> int:
        """
        Approach: Dynamic Programming
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def longestIncreasingSequence1(self, nums: List[int]) -> int:
        """
        Approach: Intelligent counting
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else: # we will replace the element
                index = 0
                while num > sub[index]:
                    index += 1
                sub[index] = num
        return len(sub)

    def longestIncreasingSequence11(self, nums: List[int]) -> int:
        """
        Approach: Intelligently Counting with Binary search scan
        T: O(N log N)
        S: O(N)
        :param nums:
        :return:
        """
        def binarySearch(subs: List[int], num: int) -> int:
            left = 0
            right = len(subs)
            while left < right:
                pivot = (left + right) // 2
                if nums[pivot] == num:
                    return pivot
                if nums[pivot] < num:
                    left = pivot + 1
                else:
                    right = pivot
            return left
        subs = [nums[0]]
        for num in nums[1:]:
            if num > subs[-1]:
                subs.append(num)
            else:
                index = binarySearch(subs, num)
                subs[index] = num
        return len(subs)


if __name__ == "__main__":
    subsequence = Subsequences()
    print(subsequence.longestIncreasingSequence([7, 7, 7, 7]))
    print(subsequence.longestIncreasingSequence([1, 3, 5, 4]))
    print(subsequence.longestIncreasingSequence([0, 1, 0, 3, 2, 3]))
    print("-*-")
    print(subsequence.longestIncreasingSequence1([7, 7, 7, 7]))
    print(subsequence.longestIncreasingSequence1([1, 3, 5, 4]))
    print(subsequence.longestIncreasingSequence([0, 1, 0, 3, 2, 3]))
    print("-*-")
    print(subsequence.longestIncreasingSequence11([7, 7, 7, 7]))
    print(subsequence.longestIncreasingSequence11([1, 3, 5, 4]))
    print(subsequence.longestIncreasingSequence([0, 1, 0, 3, 2, 3]))
