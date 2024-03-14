from typing import List


class NumberList:

    def first_missing_positive_number(self, nums: List[int]) -> int:
        """
        Approach: Index has hash key
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        if 1 not in nums:
            return 1
        size = len(nums)

        # Step 1: Flip to 1 for all nums less than equal 0 or greater than size
        for index in range(size):
            if nums[index] <= 0 or nums[index] > size:
                nums[index] = 1

        # Step 2: Based on index as hash key mark value to index negative number
        # if a number value with size is found mark it to 1st index
        for index in range(size):
            value = abs(nums[index])
            if value == size:
                nums[0] = - abs(nums[0])
            else:
                nums[value] = - abs(nums[value])
        print("nums:", nums)

        # Step 3: 1 -> n - 1 first positive encounter index will be our answer
        for index in range(1, size):
            if nums[index] > 0:
                return index

        # Step 4: if first index is positive then return size
        if nums[0] > 0:
            return size

        # Step 5: Otherwise it is size + 1
        return size + 1


if __name__ == "__main__":

    number_list = NumberList()
    print(number_list.first_missing_positive_number([2, 0, -1]))
    print(number_list.first_missing_positive_number([1, 2, 3]))
    print(number_list.first_missing_positive_number([1, 2, -1, 5]))
    print(number_list.first_missing_positive_number([1, 2, -1]))
    print(number_list.first_missing_positive_number([1, 2, 4, 5, 6]))



