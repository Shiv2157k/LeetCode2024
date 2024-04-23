class IntegerToRoman:

    def __init__(self):
        self._romanToIntMap = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def intToRoman(self, num: int) -> str:

        roman = []

        for val, symbol in self._romanToIntMap.items():
            if num > 0:
                count = num // val
                num = num % val
                roman.append(symbol * count)
            else:
                break
        return ''.join(roman)
