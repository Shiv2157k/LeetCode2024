from typing import List


class FourSum:

    def four_sum_v1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Recursion KSum
        T: O(N^3)
        S: O(N)
        :param nums:
        :param target:
        :return:
        """

        def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []

            if not nums:
                return result

            average_val = target // k

            if average_val < nums[0] or nums[-1] < average_val:
                return result

            if k == 2:
                return two_sum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for sub_set in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        result.append([nums[i]] + sub_set)
            return result

        def two_sum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            left = 0
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    result.append(nums[left], nums[right])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right += 1
            return result

        nums.sort()
        return k_sum(nums, target, 4)

    def four_sum_v0(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Two Pointers
        T: O()
        S: O()
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []

        # sort the nums
        nums.sort()
        length = len(nums)
        output = []

        for p1 in range(length - 3):

            if p1 > 0 and nums[p1 - 1] == nums[p1]:
                continue

            if nums[p1] * 4 > target:
                break

            for p2 in range(p1 + 1, length - 2):

                if p2 > p1 + 1 and nums[p2 - 1] == nums[p2]:
                    continue

                if nums[p2] * 3 > target - nums[p1]:
                    break

                p3 = p2 + 1
                p4 = length - 1

                while p3 < p4:

                    curr_sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]

                    if curr_sum == target:
                        output.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        p3 += 1
                        p4 -= 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]:
                            p3 += 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]:
                            p4 -= 1
                    elif curr_sum < target:
                        p3 += 1
                    else:
                        p4 -= 1
        return output
