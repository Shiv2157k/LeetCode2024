class ExcelSheet:

    def convert_to_title(self, column_number: int) -> str:
        """
        Approach: Math and Ord function
        T: O(N)
        S: O(1)
        :param column_number:
        :return:
        """

        result = ''

        while column_number > 0:
            column_number -= 1
            result = chr(ord('A') + column_number % 26) + result
            column_number //= 26
        return result
