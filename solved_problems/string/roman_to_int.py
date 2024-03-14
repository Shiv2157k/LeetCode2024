values = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

map = {
    "M": 1000, "CM": 900,
    "D": 500, "CD": 400,
    "C": 100, "XC": 90,
    "L": 50, "XL": 40,
    "X": 10, "IX": 9,
    "V": 5, "IV": 4,
    "I": 1
}


class RomanToInteger:

    def convertRomanToInt__(self, s: str) -> int:
        """
        Approach: Right to Left
        :param s:
        :return:
        """
        last = values[s[-1]]
        total = last

        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


    def convertRomanToInt_(self, s: str) -> int:
        """
        Approach: Improvised Left to right pass
        :param s:
        :return:
        """

        total = 0
        index = 0

        while index < len(s):
            if index + 1 < len(s) and s[index: index + 2] in map:
                total += map[s[index: index + 2]]
                index += 2
            else:
                total += map[s[index]]
                index += 1
        return total

    def convertRomanToInt(self, s: str) -> int:
        """
        Approach: Left to right pass
        :param s:
        :return:
        """

        total = 0
        index = 0

        while index < len(s):
            if index + 1 < len(s) and values[s[index]] < values[s[index + 1]]:
                total += (values[s[index + 1]] - values[s[index]])
                index += 2
            else:
                total += values[s[index]]
                index += 1
        return total


if __name__ == "__main__":
    romanToInt = RomanToInteger()
    print(romanToInt.convertRomanToInt_("MCMXCIV"))
    print(romanToInt.convertRomanToInt("MCMXCIV"))
    print(romanToInt.convertRomanToInt__("MCMXCIV"))


