from typing import List
from math import inf


class MedianOfTwoSortedArrays:

    def find_median_of_two_sorted_arrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Two Pointers and Binary Search
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
        # min length arr
        right = n1

        while left <= right:
            n1_partition = left + (right - left) // 2
            n2_partition = (n1 + n2 + 1) // 2 - n1_partition

            n1_max_left = -inf if n1_partition == 0 else nums1[n1_partition - 1]
            n1_min_right = inf if n1_partition == n1 else nums1[n1_partition]

            n2_max_left = -inf if n2_partition == 0 else nums1[n2_partition - 1]
            n2_min_right = inf if n2_partition == n2 else nums2[n2_partition]

            if n1_max_left <= n2_min_right and n2_max_left <= n1_min_right:

                if (n1 + n2) % 2 == 1:
                    return max(n1_max_left, n2_max_left)
                else:
                    return (max(n1_max_left, n2_max_left) + min(n1_min_right, n2_min_right)) / 2
            elif n1_max_left > n2_min_right:
                right = n1_partition - 1
            else:
                left = n1_partition + 1

    def find_median_of_two_sorted_arrays_v0(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Merge Sort
        T: O()
        S: O()
        :param nums1:
        :param nums2:
        :return:
        """
        n1 = len(nums1)
        n2 = len(nums2)

        p1, p2 = 0, 0

        def get_min():
            nonlocal p1, p2

            if p1 < n1 and p2 < n2:

                if nums1[p1] < nums2[p1]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n2:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (n1 + n2) % 2 == 1:
            for _ in range((n1 + n2) // 2):
                _ = get_min()
            return get_min()
        else:
            for _ in range((n1 + n2) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
