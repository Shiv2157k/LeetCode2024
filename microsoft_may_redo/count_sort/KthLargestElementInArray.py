from typing import List


class UnsortedArray:

    def kth_largest_number(self, nums: List[int], k: int) -> int:
        """
        Approach: Count Sort
        T: O(N + M)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """
        # usually we do not need min as the constraints mentions
        # array can have negative value and to account for it
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value
        return -1
