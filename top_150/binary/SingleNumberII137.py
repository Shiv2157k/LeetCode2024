from typing import List


class SingleNumberII:

    def findSingleV1(self, nums: List[int]):
        """
        Approach: Bit Manipulation (XOR and negation)
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        seenOnce, seenTwice = 0, 0

        for num in nums:
            seenOnce = (num ^ seenOnce) & (~seenTwice)
            seenTwice = (num ^ seenTwice) & (~seenOnce)
        return seenOnce

    def findSingleV0(self, nums: List[int]):

        result = 0
        bits = [0] * 32

        for i in range(32):

            for num in nums:
                bits[i] += num >> i & 1
                bits[i] %= 3

        for i in range(32):
            result = result | (bits[i] << i)
        print(bits)
        return result


if __name__ == "__main__":
    s = SingleNumberII()
    print(s.findSingleV1([10, 10, 13, 10]))
