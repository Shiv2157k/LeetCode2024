class ExcelSheet:

    def convert_to_title(self, columnNumber: int) -> str:
        """
        Approach: Base 26 Div Mod minus 1
        T: O(log N)
        S: O(1)
        :param columnNumber:
        :return:
        """
        title = ""
        while columnNumber > 0:
            # need to do this has base 26 starts from 0
            columnNumber -= 1
            # will append title at the end so that we don't have to reverse
            title = chr(ord('A') + columnNumber % 26) + title
            # we divide by 26 for next number
            columnNumber //= 26
        return title


if __name__ == "__main__":
    excel_sheet = ExcelSheet()
    print(excel_sheet.convert_to_title(26))
    print(excel_sheet.convert_to_title(27))
    print(excel_sheet.convert_to_title(1))
    print(excel_sheet.convert_to_title(9))
    print(excel_sheet.convert_to_title(2001))
    print(excel_sheet.convert_to_title(999))

