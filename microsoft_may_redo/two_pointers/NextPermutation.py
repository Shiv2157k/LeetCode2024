from typing import List


class NextPermutation:


    def generate_next_permutation(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pointers and reverse
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        size = len(nums)
        p1 = size - 2

        # move the pointer until you do not encounter increasing seq right - left
        # 1 2 4 9 8 7 6 5 3
        #     p1
        # 1 2 5 9 8 7 6 4 3
        #     -         -
        # reverse
        # 1 2 5 [3 4 6 7 8 9]
        # edge case:
        # 9 8 7 6 5 4 3 2 1
        # 1 2 3 4 5 6 7 8 9
        while p1 >= 0 and nums[p1 + 1] <= nums[p1]:
            p1 += 1

        p2 = size - 1
        if p1 >= 0:

            while nums[p2] <= nums[p1]:
                p2 -= 1

            # swap
            nums[p1], nums[p2] = nums[p2], nums[p1]
        # reverse
        left = p1 + 1
        right = size - 1

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums