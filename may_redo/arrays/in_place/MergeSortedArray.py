from typing import List


class MergeSortedArray:

    def merge_v1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        reader1 = m - 1
        reader2 = n - 1

        for writer in range(m + n - 1, -1, -1):

            if reader2 < 0:
                break
            elif reader1 >= 0 and nums1[reader1] > nums2[reader2]:
                nums1[writer] = nums1[reader1]
                reader1 -= 1
            else:
                nums1[writer] = nums2[reader2]
                reader2 -= 1

    def merge_v0(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        while p3 >= 0:

            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p3] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p3] = nums2[p2]
                    p2 -= 1
            elif p1 < 0:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1
