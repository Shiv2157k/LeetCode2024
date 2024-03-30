

class OneBits:

    def hammingWeight(self, n: int) -> int:
        """
        Approach: Kernighan's Algorithm
        n = n & (n - 1)
        T: O(1)
        S: O(1)
        :param n:
        :return:
        """
        count = 0

        while n:
            count += 1
            n = n & (n - 1)
        return count


if __name__ == "__main__":
    oneBits = OneBits()
    print(oneBits.hammingWeight(3))
    print(oneBits.hammingWeight(15))

