from typing import List


class SortedArray:

    def mergeV1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Approach: Three Pointers with for loop
        T: O(M + N)
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

            # if r1 >= 0 and r2 >= 0:
            #    if nums1[r1] > nums2[r2]:
            #        nums1[w] = nums1[r1]
            #        r1 -= 1
            #    else:
            #        nums1[w] = nums2[r2]
            #        r2 -= 1
            # elif r1 >= 0:
            #    nums1[w] = nums1[r1]
            #    r1 -= 1
            if r2 < 0:
                break
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1
        return nums1

    def mergeV0(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Approach: Three Pointers
        T: O(M + N)
        S: O(1)
        :param num1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        # brute force is to add nums2 into num1 and sort which will be O((m + n) log (m + n))

        # reader pointers
        r1 = m - 1
        r2 = n - 1
        # writer pointer
        w = m + n - 1

        while w >= 0:
            if r1 >= 0 and r2 >= 0:
                if nums2[r2] > nums1[r1]:
                    nums1[w] = nums2[r2]
                    r2 -= 1
                    w -= 1
                else:  # nums2[r2] < nums1[r1]:
                    nums1[w] = nums1[r1]
                    r1 -= 1
                    w -= 1
            elif r1 >= 0:
                nums1[w] = nums1[r1]
                w -= 1
                r1 -= 1
            else:
                nums1[w] = nums2[r2]
                w -= 1
                r2 -= 1
        return nums1


if __name__ == "__main__":
    sortedArray = SortedArray()
    print(sortedArray.mergeV0([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(sortedArray.mergeV0([1], 1, [], 0))
    print(sortedArray.mergeV0([0], 0, [1], 1))

    print(sortedArray.mergeV1([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(sortedArray.mergeV1([1], 1, [], 0))
    print(sortedArray.mergeV1([0], 0, [1], 1))
