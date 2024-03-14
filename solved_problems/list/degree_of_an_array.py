from typing import List


class Array:

    def find_shortest_sub_array(self, nums: List[int]) -> int:
        """
        Approach:
        TC: O(N)
        SC: O(N)
        :param nums:
        :return:
        """
        left, right, count = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())

        for num in nums:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        return ans


if __name__ == "__main__":

    array = Array()
    print(array.find_shortest_sub_array([1, 2, 2, 3, 1]))
    print(array.find_shortest_sub_array([1, 2]))
    print(array.find_shortest_sub_array([1, 2, 3, 1, 1]))
    print(array.find_shortest_sub_array([2, 3, 1, 1]))

