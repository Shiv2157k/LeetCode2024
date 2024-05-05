from typing import List, Dict


class PalindromicNumber:

    def largest(self, num: str) -> str:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param num:
        :return:
        """
        num_freq: Dict[str, int] = {}
        first_half: List[str] = []
        center: str = ''

        for digit in num:
            num_freq[digit] = num_freq.get(digit, 0) + 1

        for digit in range(9, -1, -1):
            char_digit = str(digit)
            if char_digit in num_freq:
                digit_count: int = num_freq[char_digit]
                num_pair: int = digit_count // 2

                if num_pair:
                    if not first_half and not digit:  # this is a zero
                        num_freq['0'] = 1
                    else:
                        first_half.append(char_digit * num_pair)
                if digit_count % 2 == 1 and center.isspace():
                    center = char_digit

        # validation check
        if not first_half and center.isspace():
            return '0'
        return "".join(first_half + [center] + first_half[::-1])
