class IntegerToRoman:

    def __init__(self):
        self._intToRomanMap = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

    def convert(self, num: int) -> str:
        """
        Approach: Greedy
        T: O(1)
        S: O(1)
        :param num:
        :return:
        """
        digitsToRoman = []

        for value, symbol in self._intToRomanMap:

            if num == 0:
                break
            count, num = num // value, num % value
            digitsToRoman.append(count * symbol)
        return "".join(digitsToRoman)


if __name__ == "__main__":
    integerToRoman = IntegerToRoman()
    print(integerToRoman.convert(1994))
    print(integerToRoman.convert(58))
