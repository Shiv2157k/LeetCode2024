from typing import List


class LargestMultipleOfThree:

    def largest_multiple_of_tree(self, digits: List[int]) -> str:

        ans = []
        mod1 = (1, 4, 7, 2, 5, 7)  # reminder 1
        mod2 = (2, 5, 8, 1, 4, 7)  # reminder 2
        count = [0] * 10
        total_sum = 0

        for digit in digits:
            count[digit] += 1
            total_sum += digit

        while total_sum % 3 != 0:

            if total_sum % 3 == 1:
                mod = mod1
            else:
                mod = mod2
            found = False
            for num in mod:
                if count[num] > 0:
                    count[num] -= 1
                    total_sum -= num
                    found = True
                    break

            if not found:
                return ''

        if sum(count) == 0:
            return ''

        for digit in range(9, -1, -1):
            ans.extend([str(digit)] * count[digit])

        result = ''.join(ans)
        return '0' if not result or result[0] == '0' else result