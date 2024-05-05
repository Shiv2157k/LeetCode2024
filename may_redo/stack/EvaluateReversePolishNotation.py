from typing import List


class ReversePolishNotation:

    def eval_rpn(self, tokens: List[str]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param tokens:
        :return:
        """

        stack: List[int] = []

        for token in tokens:

            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
                continue

            val2 = stack.pop()
            val1 = stack.pop()

            result = 0
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                result = int(val1 / val2)

            stack.append(result)
        return stack.pop()
