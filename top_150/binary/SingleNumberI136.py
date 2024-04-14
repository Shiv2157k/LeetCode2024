from typing import List


class SingleNumber:

    def findNumberV1(self, nums: List[int]) -> int:
        """
        Approach: XOR Bit Manipulation
        A xor B === (A + B) // 2
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        output = 0

        for num in nums:
            output = output ^ num
        return output

    def findNumberV0(self, nums: List[int]) -> int:
        """
        Approach: Freq with HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for num in freqMap:
            if freqMap[num] == 1:
                return num
        
