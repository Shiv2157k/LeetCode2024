class IntegerToRoman:

    def __init__(self):
        self._integer_map = {
            1000: 'M',
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

    def integer_to_roman(self, num: int) -> str:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param num:
        :return:
        """

        roman_number = []

        for value, symbol in self._integer_map.items():

            if num > 0:
                count = num // value
                num %= value
                roman_number.append(count * symbol)
            else:
                break
        return ''.join(roman_number)
