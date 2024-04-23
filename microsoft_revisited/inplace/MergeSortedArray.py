from typing import List


class SortedArray:

    def mergeV0(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Approach: Two Pointers
        T: O(m + n)
        S: O(1)
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        while p3 >= 0:

            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p3] = nums1[p1]
                    p3 -= 1
                    p1 -= 1
                else:
                    nums1[p3] = nums2[p2]
                    p3 -= 1
                    p2 -= 1
            elif p1 < 0:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1

    def mergeV1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Approach: Two Pointers
        T: O(m + n)
        S: O(1)
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """

        r1 = m - 1
        r2 = n - 1

        for w in range(m + n - 1, -1, -1):

            if r2 < 0:
                break
            elif r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1
