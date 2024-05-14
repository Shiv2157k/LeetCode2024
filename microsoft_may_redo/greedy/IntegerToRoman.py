class IntegerToRoman:

    def int_to_roman(self, num: int) -> str:
        """
        Approach: Greedy with hashmap
        T: O(N)
        S: O(1)
        :param num:
        :return:
        """

        int_to_roman_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
            4: 'IV', 1: 'I'
        }

        output = []

        for value, symbol in int_to_roman_map.items():

            if num > 0:
                count = num // value
                num %= value
                output.append(symbol * count)
            else:
                break
        return ''.join(output)
