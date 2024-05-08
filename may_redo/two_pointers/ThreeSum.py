from typing import List


class ThreeSum:

    def three_sum(self, nums: List[List[int]]) -> List[List[int]]:
        """
        Approach: Two Pointers
        T: O(N^2)
        S: O(1)
        :param nums:
        :return:
        """

        nums.sort()
        result = []
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if i == 0 or nums[i] != nums[i - 1]:
                self._get_three_sum_pairs(nums, i, result)
        return result

    def _get_three_sum_pairs(self, nums: List[int], p1: int, result: List[List[int]]):
        p2 = p1 + 1
        p3 = len(nums) - 1

        while p2 < p3:
            curr_sum = nums[p1] + nums[p2] + nums[p3]

            if curr_sum == 0:
                result.append([nums[p1], nums[p2], nums[p3]])
                p2 += 1
                p3 -= 1

                while p2 < p3 and nums[p2] == nums[p2 - 1]:
                    p2 += 1
                while p2 < p3 and nums[p3] == nums[p3 + 1]:
                    p3 -= 1
            elif curr_sum < 0:
                p2 += 1
            else:
                p3 -= 1
