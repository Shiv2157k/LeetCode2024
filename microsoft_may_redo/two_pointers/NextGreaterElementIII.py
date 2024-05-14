

class NextGreaterElement:

    def next_greater_element(self, n: int) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """

        nums = list(str(n))

        p1 = len(nums) - 2

        # stop pointer when val is greater than the right side value
        while p1 >= 0 and nums[p1 + 1] <= nums[p1]:
            p1 -= 1

        if p1 < 0:
            return -1

        p2 = len(nums) - 1
        # stop pointer when encountered a number > p2
        while p2 >= 0 and nums[p2] <= nums[p2]:
            p2 -= 1

        nums[p1], nums[p2] = nums[p2], nums[p1]
        left = p1 + 1
        right = len(nums) - 1
        # reverse
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        result = 0
        for num in nums:
            result += (result * 10) + (ord(num) - ord('0'))
        return result if result <= 2**31-1 else -1