from typing import List, Union


class RemoveAllAdjacentDuplicatesInString:

    def remove_duplicates(self, s: str, k: int) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """

        stack: List[List[Union[str, int]]] = []

        for char in s:

            if stack and stack[1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ""
        for char, freq in stack:
            result += (char * freq)
        return result
