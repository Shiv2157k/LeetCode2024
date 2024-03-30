



class InputBits:


    def reverseBits(self, n: int) -> int:
        """
        Bit by bit manipulation
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """

        ret = 0
        power = 31

        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


if __name__ == "__main__":
    inputBits = InputBits()
    print(inputBits.reverseBits(3))