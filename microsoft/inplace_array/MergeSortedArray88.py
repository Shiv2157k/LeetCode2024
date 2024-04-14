from typing import List


class MergeSortedArray:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Approach: Three Pointers
        T: O(N)
        S: O(1)
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """

        p3 = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p3 >= 0:

            if p1 >= 0 and p2 >= 0:
                if nums1[p1] < nums2[p2]:
                    nums1[p3] = nums2[p2]
                    p3 -= 1
                    p2 -= 1
                else:
                    nums1[p3] = nums1[p1]
                    p3 -= 1
                    p1 -= 1
            elif p1 >= 0:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
