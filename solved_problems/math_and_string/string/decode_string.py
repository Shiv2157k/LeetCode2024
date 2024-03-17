class String:
    
    def decode(self, s: str) -> str:
        """
        Approach Explanation:
        The idea is to read symbol by symbol and check options:

        - If we see digit, it means that we need to form number,
          so just do it: multiply already formed number by 10 and add this digit.
        - If we see open bracket [, it means, that we just right before finished to form our number:
          so we put it into our stack. Also we put in our stack empty string.
        - If we have close bracket ], it means that we just finished [...] block and
          what we have in our stack: on the top it is solution for what we have inside bracktes,
          before we have number of repetitions of this string rep and finally,
          before we have string built previously: so we concatenate str2 and str1 * rep.
        - Finally, if we have some other symbol, that is letter, we add it the the last element of our stack.
        - For better understanding the process,
          let us consider example s = 3[a5[c]]4[b]:
            [''] at first we have stack with empty string.
            ['', 3, ''], open bracket: now we have stack with 3 elements: empty string, number 3 and empty string.
            ['', 3, 'a']: build our string
            ['', 3, 'a', 5, ''], open bracket: add number and empty string
            ['', 3, 'a', 5, 'c'] build string
            ['', 3, 'accccc'] : now we have closing bracket, so we remove last 3 elements and put accccc into our stack
            ['acccccacccccaccccc'] we again have closing bracket, so we remove last 3 elements and put new one.
            ['acccccacccccaccccc', 4, '']: open bracket, add number and empty string to stack
            ['acccccacccccaccccc', 4, 'b'] build string
            ['acccccacccccacccccbbbb'] closing bracket: remove last 3 elements and put one new.
        Finally, return joined strings from our stack.
        Complexity:
            we can say, that time and space complexity is O(m), where m is size of our answer.
            Potentially it can be very big, for strings like 999999999999999[a],
        :return:
        """
        stack, digit = [''], 0
        for char in s:
            # check digit
            if char.isdigit():
                digit = digit * 10 + int(char)
            # check open bracket
            elif char == '[':
                stack.append(digit)
                digit = 0
                stack.append('')
            # check close bracket
            elif char == ']':
                expr = stack.pop()
                multiplier = stack.pop()
                prefix = stack.pop()
                stack.append(prefix + expr * multiplier)
            # otherwise add the char to the last char of the stack
            else:
                stack[-1] += char
        return ''.join(stack)


if __name__ == "__main__":
    string = String()
    print(string.decode("3[a5[c]]4[b]"))
    print(string.decode("4[b]"))
    print(string.decode("2[b3[c]]"))

