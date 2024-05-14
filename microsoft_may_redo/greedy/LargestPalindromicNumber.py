class LargestPalindromicNumber:

    def largest_palindromic(self, num: str) -> str:
        """
        Approach: Greedy + HashMap for freq
        T: O(N)
        S: O(N)
        :param num:
        :return:
        """
        num_freq = {}
        output = []
        center = ''

        for digit in num:
            num_freq[digit] = num_freq.get(digit, 0) + 1

        for digit in range(9, -1, -1):
            char_digit = str(digit)

            if char_digit in num_freq:

                digit_counts = num_freq[char_digit]
                pairs = digit_counts // 2

                if pairs > 0:

                    if not output and digit == 0:
                        num_freq['0'] = 1
                    else:
                        output.append(char_digit * pairs)
                if digit_counts % 2 == 1 and center == '':
                    center = char_digit

        if not output and center == '':
            return '0'

        output.append(center)
        length = len(output)
        for ptr in range(length - 2, -1, -1):
            output.append(output[ptr])
        return ''.join(output)
