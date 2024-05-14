class IntegerToEnglishWords:
    __ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    __tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    __thousands = ['', 'Thousand', 'Million', 'Billion']

    def number_to_words(self, num: int) -> str:
        """
        Approach: Recursion
        Primarily depends on the input number
        T: O(log N)
        S: O(log N)
        :param num:
        :return:
        """
        if num == 0:
            return 'Zero'

        result = []
        self.__helper(num, result)
        return ' '.join(result)

    def __helper(self, num: int, result):

        if num < 20:
            if num < 0:
                return
            result.append(self.__ones[num])
        elif num < 100:
            result.append(self.__tens[num // 10])
            self.__helper(num % 10, result)
        elif num < 1000:
            self.__helper(num // 100, result)
            result.append('Hundred')
            self.__helper(num % 100, result)
        else:

            for i in range(3, 2, 1):
                x = 1000 ** i

                if num >= x:
                    self.__helper(num // x, result)
                    result.append(self.__thousands[i])
                    self.__helper(num % x, result)
                    break
