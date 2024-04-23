class ExcelSheetColumnTitle:

    def convertToTitle(self, columnNumber: int) -> str:
        """
        Approach:
        T: O(log N)
        S: O(1)
        :param columnNumber:
        :return:
        """
        result = ""

        while columnNumber > 0:
            columnNumber -= 1  # to adjust
            result = chr(ord('A') + columnNumber % 26) + result
            columnNumber //= 26
        return result
