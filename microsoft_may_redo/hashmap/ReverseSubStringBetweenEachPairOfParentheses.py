class StringWithParentheses:

    def reverse_substr_with_each_pair(self, s: str) -> str:
        """
        Approach:
        Parentheses HashMap with left and right index reference
        (Worm Approach) combining open bracket stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        pair_index = {}
        open_bracket_stack = []

        for i, char in enumerate(s):

            if char == '(':
                open_bracket_stack.append(i)
            elif char == ')':
                x = open_bracket_stack.pop()
                pair_index[x] = i
                pair_index[i] = x

        result = []
        delta = 1

        ptr = 0

        while ptr < len(s):

            if s[ptr] in {'(', ')'}:
                ptr = pair_index[ptr]
                delta *= -1
            else:
                result.append(s[ptr])
            ptr += delta
        return ''.join(result)
