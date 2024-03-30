from typing import List


class Bits:


    def countingBitsV1(self, n: int) -> List[int]:
        """
        Approach: DP + Last Set Bit
        T: O(n)
        S: O(1)
        :param n:
        :return:
        """
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans
    def countingBitsV0(self, n: int) -> List[int]:
        """
        Approach: Pop Count
        T: O(N log N) <- O(n⋅log(n)/2)
        S: O(1)
        :param n:
        :return:
        """

        def popCount(x: int):
            count = 0

            while x:
                count += 1
                x = x & (x - 1)
            return count

        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = popCount(i)
        return ans


if __name__ == "__main__":
    bits = Bits()
    print(bits.countingBitsV0(5))
    print(bits.countingBitsV0(3))

    print(bits.countingBitsV1(5))
    print(bits.countingBitsV1(3))
