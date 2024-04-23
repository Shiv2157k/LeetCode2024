from typing import List


class MedianOfTwoSortedArrays:

    def getMedianV0(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Merge Sort
        T: O(N + M)
        S: O(1)
        :param nums1:
        :param nums2:
        :return:
        """

        p1, p2 = 0, 0
        n = len(nums1)
        m = len(nums2)

        def getMin():
            nonlocal p1, p2
            if p1 < n and p2 < m:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == m:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0:  # even
            for _ in range((m + n) // 2 - 1):
                _ = getMin()
            return (getMin() + getMin()) / 2
        else:
            for _ in range((m + n) // 2):
                _ = getMin()
            return getMin()

    def getMedianV1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach:
        T: O(log(min(n1, n2)
        S: O(1)
        :param nums1:
        :param nums2:
        :return:
        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)

        left, right = 0, min(n1, n2)

        while left <= right:

            n1Partition = left + (right - left) // 2
            n2Partition = (n1 + n2 + 1) // 2 - n1Partition

            n1LeftMax = float('-inf') if n1Partition == 0 else nums1[n1Partition - 1]
            n1RightMin = float('inf') if n1Partition == n1 else nums1[n1Partition]

            n2LeftMax = float('-inf') if n2Partition == 0 else nums2[n2Partition - 1]
            n2RightMin = float('inf') if n2Partition == n2 else nums2[n2Partition]

            if n1LeftMax <= n2RightMin and n2LeftMax <= n1RightMin:

                if (n1 + n2) % 2 == 1:
                    return max(n1LeftMax, n2LeftMax)
                else:
                    return (max(n1LeftMax, n2LeftMax) + min(n1RightMin, n2RightMin)) / 2
            elif n1LeftMax > n2RightMin:
                right = n1Partition - 1
            else:
                left = n1Partition + 1
