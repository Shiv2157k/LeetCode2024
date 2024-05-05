from typing import List


class Polygon:

    def with_largest_perimeter(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N log N)
        S: O(1)
        :param nums:
        :return:
        """
        # helps with easy simulation
        nums.sort()

        sum_so_far = 0
        largest_perimeter = -1

        for num in nums:
            if num < sum_so_far:
                largest_perimeter = num + sum_so_far
            sum_so_far += num
        return largest_perimeter
