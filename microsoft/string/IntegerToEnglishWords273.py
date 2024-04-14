from typing import List


class IntegerToEnglishWords:
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"
        result = []
        self.helper(num, result)
        return " ".join(result)

    def helper(self, num: int, result: List[str]):

        if num < 20:
            if num == 0:
                return
            result.append(self.ones[num])
        elif num < 100:
            result.append(self.tens[num // 10])
            self.helper(num % 10, result)
        elif num < 1000:
            self.helper(num // 100, result)
            result.append("Hundred")
            self.helper(num % 100, result)
        else:

            for i in {3, 2, 1}:
                x = 1000 ** i
                if num >= x:
                    self.helper(num // x, result)
                    result.append(self.thousands[i])
                    self.helper(num % x, result)
                    break
