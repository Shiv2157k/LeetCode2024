class ExcelSheetColumnNumber:

    def title_to_number(self, column_title: str) -> int:
        """
        Approach: ORd and math
        T: O(N)
        S: O(1)
        :param column_title:
        :return:
        """

        number = 0
        for char in column_title:
            number *= 26
            number += (ord(char) - ord('A') + 1)
        return number
