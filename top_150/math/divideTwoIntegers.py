class DivideIntegers:

    def divideV2(self, dividend: int, divisor: int) -> float:
        """
        Approach:
        T: O(log N)
        S: O(N)
        :param dividend:
        :param divisor:
        :return:
        """

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = -2**31 // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = 2
        if dividend > 0:
            dividend = -dividend
            negative -= 1
        if divisor > 0:
            divisor = -divisor
            negative -= 1

        powersOfTwo = []
        doubles = []
        powerOfTwo = 1

        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)

            if divisor < HALF_MIN_INT:
                break
            divisor += divisor  # double the divisor
            powerOfTwo += powerOfTwo

        quotient = 0

        for i in range(len(doubles) - 1, -1, -1):

            if doubles[i] >= dividend:
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
        return quotient if negative != 1 else -quotient

    def divideV1(self, dividend: int, divisor: int) -> float:
        """
        Approach: Exponential
        T: O(log ^2 * n)
        S: O(1)
        :param dividend:
        :param divisor:
        :return:
        """

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = 2

        if dividend > 0:
            dividend = -dividend
            negative -= 1
        if divisor > 0:
            divisor = -divisor
            negative -= 1

        quotient = 0

        while divisor >= dividend:

            value = divisor
            powerOfTwo = -1

            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value
        return -quotient if negative != 1 else quotient

    def divideV0(self, dividend: int, divisor: int) -> float:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param dividend:
        :param divisor:
        :return:
        """

        MAX_INT = 2147483647
        MIN_INT = -2147483648

        # edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2

        if dividend > 0:
            dividend = -dividend
            negatives -= 1
        if divisor > 0:
            divisor = -divisor
            negatives -= 1

        quotient = 0
        while dividend - divisor <= 0:
            quotient -= 1
            dividend -= divisor
        return -quotient if negatives != 1 else quotient


if __name__ == "__main__":
    divideIntegers = DivideIntegers()
    print(divideIntegers.divideV1(10, 3))
    print(divideIntegers.divideV2(10, 3))
    print(divideIntegers.divideV0(10, 3))
