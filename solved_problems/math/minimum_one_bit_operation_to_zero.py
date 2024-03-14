class BitOperation:

    def minimum_to_make_zero_v1(self, n: int) -> int:
        """
        Approach: Iterative
        T: O()
        S: O()
        :param n:
        :return:
        """

        x = '{0: b}'.format(n)
        is_right = True
        result = 0

        for k in range(len(x)):
            if x[k] == "1" and is_right:
                result += (2**(len(x) - k)) - 1
                is_right = False
            elif x[k] == "1":
                result -= (2**(len(x) - k)) - 1
                is_right = True
        return result


    def minimum_to_make_zero(self, n: int) -> int:
        """
        Recursion
        T: O(2*log2^n)
        S: O(log2^n)
        :param n:
        :return:
        """
        if n == 0:
            return 0
        k = 0
        while 2 ** k <= n:
            k += 1
        k -= 1
        return 2 ** (k + 1) - 1 - self.minimum_to_make_zero(2 ** k ^ n)


if __name__ == "__main__":
    bit_operation = BitOperation()
    print(bit_operation.minimum_to_make_zero(10))
    print(bit_operation.minimum_to_make_zero(4))
    print(bit_operation.minimum_to_make_zero(3))
    print(bit_operation.minimum_to_make_zero(2))
    print(bit_operation.minimum_to_make_zero(1))
    print("***+****")
    print(bit_operation.minimum_to_make_zero_v1(10))
    print(bit_operation.minimum_to_make_zero_v1(4))
    print(bit_operation.minimum_to_make_zero_v1(3))
    print(bit_operation.minimum_to_make_zero_v1(2))
    print(bit_operation.minimum_to_make_zero_v1(1))

