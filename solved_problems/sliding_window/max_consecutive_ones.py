from typing import List


class ConsecutiveOnes:

    def find_longest_with_k_flips(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        right = 0
        left = 0
        while right < len(nums):
            # decrement k when a zero is encountered
            k -= 1 - nums[right]
            # if k is less than 0 we have reached the flip limit
            if k < 0:
                # increment k if the left element going to throw out from the window is zero
                k += 1 - nums[left]
                left += 1
            right += 1
        return right - left


if __name__ == "__main__":
    consecutiveOnes = ConsecutiveOnes()
    print(consecutiveOnes.find_longest_with_k_flips([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(consecutiveOnes.find_longest_with_k_flips([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

