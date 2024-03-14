from typing import List


class Array:

    def subArraySumEqualsK(self, nums: List[int], k: int) -> int:
        """
        Approach: Cumulative Sum
        T: O(N^2)
        S: O(1)
        """
        count = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

    def subArraySumEqualsK1(self, nums: List[int], k: int) -> int:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """
        sumOccurenceMap = {0: 1}
        count = 0
        cummulativeSum = 0

        for i in range(len(nums)):
            cummulativeSum += nums[i]
            if (cummulativeSum - k) in sumOccurenceMap:
                count += sumOccurenceMap[cummulativeSum - k]
            sumOccurenceMap[cummulativeSum] = sumOccurenceMap.get(cummulativeSum, 0) + 1
        return count


if __name__ == "__main__":
    array = Array()
    print(array.subArraySumEqualsK([1, 1, 1], 2))
    print(array.subArraySumEqualsK([1, 2, 3], 3))
    print(array.subArraySumEqualsK([3, 4, 7, 2, -3, 7, 4, 2], 7))
    print(array.subArraySumEqualsK1([1, 1, 1], 2))
    print(array.subArraySumEqualsK1([1, 2, 3], 3))
    print(array.subArraySumEqualsK1([3, 4, 7, 2, -3, 7, 4, 2], 7))
