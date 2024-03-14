from typing import List


class MinimumSizeSubArray:

    def get_v0(self, nums: List[int], target: int) -> int:
        """
        Brute Force
        :param nums:
        :param target:
        :return:
        """
        min_size = float("inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(j, len(nums)):
                    sum += nums[k]
                    if sum >= target:
                        min_size = min(min_size, j - i + 1)
                        break
        return min_size if min_size != float("inf") else 0

    def get(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """
        left = right = total_sum = 0
        min_size = float("inf")

        while right < len(nums):
            total_sum += nums[right]
            while total_sum >= target:
                min_size = min(min_size, right - left + 1)
                total_sum -= nums[left]
                left += 1
            right += 1
        return min_size if min_size != float("inf") else 0


if __name__ == "__main__":
    arr = MinimumSizeSubArray()
    print(arr.get([4, 5, 2, 3, 1], 6))
    print(arr.get([4, 5, 2, 3, 1], 7))
    print(arr.get([4, 5, 2, 3, 1], 11))
    print(arr.get([4, 5, 2, 3, 1], 1))
    print("**__**")
    print(arr.get([4, 5, 2, 3, 1], 6))
    print(arr.get([4, 5, 2, 3, 1], 7))
    print(arr.get([4, 5, 2, 3, 1], 11))
    print(arr.get([4, 5, 2, 3, 1], 1))

