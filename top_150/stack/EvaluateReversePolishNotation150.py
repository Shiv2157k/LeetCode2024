from typing import List


class ReversePolishNotation:

    def evaluate(self, tokens: List[str]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param tokens:
        :return:
        """

        stack = []

        for token in tokens:

            if not token in {"+", "*", "/", "-"}:
                stack.append(int(token))
                continue

            n2 = stack.pop()
            n1 = stack.pop()
            result = 0
            if token == "+":
                result = n1 + n2
            elif token == "-":
                result = n1 - n2
            elif token == "*":
                result = n1 * n2
            else:
                result = int(n1 / n2)
            stack.append(result)
        return stack.pop()


if __name__ == "__main__":
    rpn = ReversePolishNotation()
    print(rpn.evaluate(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
