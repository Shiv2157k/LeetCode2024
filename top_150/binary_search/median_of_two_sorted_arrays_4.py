from typing import List


class TwoSortedArrays:

    def findMedianV2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search Optimized
        T: O()
        S: O()
        :param nums1:
        :param nums2:
        :return:
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l1, l2 = len(nums1), len(nums2)

        left, right = 0, l1

        while left <= right:
            nums1Partition = left + (right - left) // 2
            nums2Partition = (l1 + l2 + 1) // 2 - nums1Partition

            nums1LeftMax = float("-inf") if nums1Partition == 0 else nums1[nums1Partition - 1]
            nums1RightMin = float("inf") if nums1Partition == l1 else nums1[nums1Partition]

            nums2LeftMax = float("-inf") if nums2Partition == 0 else nums2[nums2Partition - 1]
            nums2RightMin = float("inf") if nums2Partition == l2 else nums2[nums2Partition]

            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:

                if (l1 + l2) % 2 == 1:
                    return max(nums1LeftMax, nums2LeftMax)
                else:
                    return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
            elif nums1LeftMax > nums2RightMin:
                right = nums1Partition - 1
            else:
                left = nums1Partition + 1

    def findMedianV1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search Recursion
        T: O(log(m * n))
        S: O(log m + log n)
        :param nums1:
        :param nums2:
        :return:
        """
        l1, l2 = len(nums1), len(nums2)

        def solve(k: int, nums1Left: int, nums1Right: int, nums2Left: int, nums2Right: int) -> float:

            if nums1Left > nums1Right:
                return nums2[k - nums1Left]
            if nums2Left > nums2Right:
                return nums2[k - nums2Left]

            nums1PartitionIndex = nums1Left + (nums1Right - nums1Left) // 2
            nums2PartitionIndex = nums2Left + (nums2Right - nums2Left) // 2

            nums1Val = nums1[nums1PartitionIndex]
            nums2Val = nums2[nums2PartitionIndex]

            if k > nums1PartitionIndex + nums2PartitionIndex:

                if nums1Val > nums2Val:
                    return solve(k, nums1Left, nums1Right, nums2PartitionIndex + 1, nums2Right)
                else:
                    return solve(k, nums1PartitionIndex + 1, nums1Right, nums2Right, nums2Right)
            else:
                if nums1Val > nums2Val:
                    return solve(k, nums1Left, nums1PartitionIndex - 1, nums2Left, nums2Right)
                else:
                    return solve(k, nums1Left, nums1Right, nums2Left, nums2PartitionIndex - 1)

        if (l1 + l2) % 2 == 1:
            return solve((l1 + l2) // 2, 0, l1 - 1, 0, l2 - 1)
        else:
            return (solve((l1 + l2) // 2 - 1, 0, l1 - 1, 0, l2 - 1) + solve((l1 + l2) // 2, 0, l1 - 1, 0, l2 - 1)) / 2

    def findMedianV0(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Merge Sort
        T: O(M + N)
        S: O(1)
        :param nums1:
        :param nums2:
        :return:
        """
        nums1Len = len(nums1)
        nums2Len = len(nums2)

        # two pointers
        p1, p2 = 0, 0

        def getMin() -> int:
            nonlocal p1, p2
            if p1 < nums1Len and p2 < nums2Len:

                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p1 == nums1Len:
                ans = nums2[p2]
                p2 += 1
            else:
                ans = nums1[p1]
                p1 += 1
            return ans

        # odd length
        if (nums1Len + nums2Len) % 2 == 1:
            for _ in range((nums1Len + nums2Len) // 2):
                _ = getMin()
            return getMin()
        else:  # even length
            for _ in range((nums1Len + nums2Len) // 2 - 1):
                _ = getMin()
            return (getMin() + getMin()) / 2


if __name__ == "__main__":
    twoSortedArrays = TwoSortedArrays()
    print(twoSortedArrays.findMedianV0([1, 2], [3, 4]))
    print(twoSortedArrays.findMedianV0([1, 3], [2]))
