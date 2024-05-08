class ReverseSubStringBetweenEachPair:

    def reverse_parentheses(self, s: str) -> str:
        """
        Approach: Worm holes / Two Pass with stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        open_brackets_stack = []
        pair_occurrence = {}

        for i, char in enumerate(s):

            if char == '(':
                open_brackets_stack.append(i)
            if char == ')':
                open_pair_ptr = open_brackets_stack.pop()
                pair_occurrence[open_pair_ptr] = i
                pair_occurrence[i] = open_pair_ptr

        ptr = 0
        delta = 1
        result = []

        while ptr < len(s):

            if s[ptr] in {')', '('}:
                ptr = pair_occurrence[ptr]
                delta *= -1
            else:
                result.append(s[ptr])
            ptr += delta
        return ''.join(result)


if __name__ == "__main__":
    rev = ReverseSubStringBetweenEachPair()
    print(rev.reverse_parentheses("(ed(et(oc))el)"))
