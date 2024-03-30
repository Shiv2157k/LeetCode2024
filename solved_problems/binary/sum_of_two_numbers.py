class TwoNumbers:

    def sumV1(self, a: int, b: int) -> int:
        """
        Approach: Two's Complement and Bit MAsk
        T: O(1)
        S: O(1)
        :param a:
        :param b:
        :return:
        """
        # The hexadecimal number 0xFFFFFFFF represents
        # the maximum value for a 32-bit unsigned integer.
        # In binary, it is represented as:
        # 1111 1111 1111 1111 1111 1111 1111 1111
        mask = 0xFFFFFFFF
        while b != 0:
            # a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            x = (a ^ b) & mask
            y = ((a & b) << 1) & mask
            a, b = x, y
        # 0x7FFFFFFF represents the hexadecimal representation of
        # the maximum positive value for a 32-bit signed integer.
        # In binary, it is represented as:
        # 0111 1111 1111 1111 1111 1111 1111 1111
        # This binary number represents 2^31 - 1,
        # which is 2147483647 in decimal notation.
        # This is the largest positive value
        # that can be represented using a 32-bit signed integer.
        maxInt = 0x7FFFFFFF
        return a if a < maxInt else ~(a ^ mask)

    def sumV0(self, a: int, b: int) -> int:
        """
        Approach: Bit Manipulation
        T: O(1) -> each integer contains 32 bits
        S: O(1) -> no additional space
        :param a:
        :param b:
        :return:
        """
        x, y = abs(a), abs(b)

        if x < y:
            return self.sumV0(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:

            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x = answer
                y = carry
        else:
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x = answer
                y = borrow
        return x * sign


if __name__ == "__main__":
    twoNumbers = TwoNumbers()
    print(twoNumbers.sumV0(15, 19))
    print(twoNumbers.sumV0(15, 15))
    print(twoNumbers.sumV0(15, 4))
    print(twoNumbers.sumV0(-15, 4))
    print(twoNumbers.sumV0(15, -4))
    print(twoNumbers.sumV0(-15, -4))
    print("____^^^^____")
    print(twoNumbers.sumV1(15, 19))
    print(twoNumbers.sumV1(15, 15))
    print(twoNumbers.sumV1(15, 4))
    print(twoNumbers.sumV1(-15, 4))
    print(twoNumbers.sumV1(15, -4))
    print(twoNumbers.sumV1(-15, -4))
