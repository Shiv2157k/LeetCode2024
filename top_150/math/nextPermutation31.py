from typing import List


class Permutation:

    def getNext(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Pass Approach
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        size = len(nums)
        if not size or size == 1:
            return nums

        ptr1 = size - 1

        # Step 1: Point to the non-decreasing number from the back of list
        # 1, 2, 4, 5, 3
        #          p1
        while ptr1 >= 1 and nums[ptr1] <= nums[ptr1 - 1]:
            ptr1 -= 1

        ptr2 = size - 1
        if ptr1 != 0:
            # 1,   2,   4,   5,   3
            #          p1-1  p1   p2
            #                p2
            while nums[ptr2] <= nums[ptr1 - 1]:
                ptr2 -= 1

        # swap p1 - 1 and p2
        # 1,   2,   4,     5,    3
        #          p1 - 1  p1    p2
        # 1,   2,   5,     4,    3
        nums[ptr1 - 1], nums[ptr2] = nums[ptr2], nums[ptr1 - 1]

        # reverse from p1 to size - 1
        # 1, 2, 5, [4, 3] -> reverse
        left, right = ptr1, size - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == "__main__":
    permutation = Permutation()
    print(permutation.getNext([1, 2, 4, 5, 3]))
