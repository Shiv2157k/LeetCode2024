from typing import List


class ThreeSum:

    def unique_three_sum_values_v2(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointer
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        result = []
        if not nums:
            return result
        # sort nums to avoid duplicates
        nums.sort()
        for index in range(len(nums)):
            if nums[index] > 0:
                break
            if index == 0 or nums[index - 1] != nums[index]:
                self._two_sum_ii(nums, index, result)
        return result

    def _two_sum_ii(self, nums: List[int], pre_index: int, result: List[List[int]]) -> None:
        left, right = pre_index + 1, len(nums) - 1
        while left < right:
            target = nums[pre_index] + nums[left] + nums[right]
            if target < 0:
                left += 1
            elif target > 0:
                right -= 1
            else:
                result.append([nums[pre_index], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    def unique_three_sum_values_v1(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Hash Set
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        result = []
        if not nums:
            return result
        nums.sort()

        for index in range(len(nums)):
            if nums[index] > 0:
                break
            if index == 0 or nums[index] != nums[index - 1]:
                self._two_sum(nums, index, result)
        return result

    def _two_sum(self, nums: List[int], pre_index: int, result: List[List[int]]) -> None:
        curr_index = pre_index + 1
        seen = set()
        while curr_index < len(nums):
            complement = -nums[pre_index] - nums[curr_index]
            if complement in seen:
                result.append([nums[pre_index], nums[curr_index], complement])
                while curr_index + 1 < len(nums) and nums[curr_index] == nums[curr_index + 1]:
                    curr_index += 1
            seen.add(nums[curr_index])
            curr_index += 1

    def unique_three_sum_values_v0(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Hash Set Not Sorted
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        result, duplicates = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in duplicates:
                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2
                    if complement in seen:
                        result.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return result


if __name__ == "__main__":
    three_sum = ThreeSum()
    print(three_sum.unique_three_sum_values_v0([-1, 0, 1, 2, -1, -4]))
    print(three_sum.unique_three_sum_values_v1([-1, 0, 1, 2, -1, -4]))
    print(three_sum.unique_three_sum_values_v2([-1, 0, 1, 2, -1, -4]))
    print("***__***")
    print(three_sum.unique_three_sum_values_v0([0, 1, 1]))
    print(three_sum.unique_three_sum_values_v1([0, 1, 1]))
    print(three_sum.unique_three_sum_values_v2([0, 1, 1]))
    print("***__***")
    print(three_sum.unique_three_sum_values_v0([0, 0, 0]))
    print(three_sum.unique_three_sum_values_v1([0, 0, 0]))
    print(three_sum.unique_three_sum_values_v2([0, 0, 0]))
