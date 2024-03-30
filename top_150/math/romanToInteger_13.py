

class RomanToInteger:

    def __init__(self):

        self._romanMap = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

    def convert(self, s: str) -> int:
        """
        Approach: Greedy
        T: O(1)
        S: O(1)
        :param s:
        :return:
        """
        digits = 0
        pointer = 0
        while pointer < len(s):
            if pointer + 1 < len(s) and self._romanMap[s[pointer]] < self._romanMap[s[pointer + 1]]:
                digits = digits + (self._romanMap[s[pointer + 1]] - self._romanMap[s[pointer]])
                pointer += 2
            else:
                digits += self._romanMap[s[pointer]]
                pointer += 1
        return digits


if __name__ == "__main__":

    romanToInteger = RomanToInteger()
    print(romanToInteger.convert("MCMXCIV"))
    print(romanToInteger.convert("LVIII"))