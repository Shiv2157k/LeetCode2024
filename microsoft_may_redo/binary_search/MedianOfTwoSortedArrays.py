from typing import List
from math import inf


class MedianOfTwoSortedArrays:

    def find_median(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search on two lists
        T: O(log(min(m, n)))
        S: O(1)
        :param nums1:
        :param nums2:
        :return:
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)

        left = 0
        right = n1

        while left <= right:
            n1_partition = left + (right - left) // 2
            n2_partition = (n1 + n2 + 1) // 2 - n1_partition

            n1_left_max = -inf if n1_partition == 0 else nums1[n1_partition - 1]
            n1_right_min = inf if n1_partition == n1 else nums1[n1_partition]

            n2_left_max = -inf if n2_partition == 0 else nums2[n2_partition - 1]
            n2_right_min = inf if n2_partition == n2 else nums2[n2_partition]

            if n1_left_max <= n2_right_min and n2_left_max <= n1_right_min:
                if (n1 + n2) % 2 == 1:
                    return max(n1_left_max, n2_left_max)
                else:
                    return (max(n1_left_max, n2_left_max) + min(n1_right_min, n2_right_min)) / 2
            elif n1_left_max > n2_right_min:
                right = n1_partition - 1
            else:
                left = n1_partition + 1
