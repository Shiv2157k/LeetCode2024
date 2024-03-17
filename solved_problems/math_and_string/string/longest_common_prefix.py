from typing import List


class Prefix:

    def find_longest_common_prefix(self, string: List[str]) -> str:
        """
        Binary Search
        Time Complexity: O(S log n)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        # validation
        if not string:
            return ""

        left, right = 0, len(min(string, key=len))

        while left <= right:
            pivot = (left + right) // 2
            prefix = string[0][:pivot]
            if all(s.startswith(prefix) for s in string[1:]):
                left = pivot + 1
            else:
                right = pivot - 1
        return string[0][:(left + right) // 2]

    def find_longest_common_prefix_(self, string: List[str]) -> str:
        """
        Min and Max approach
        :param string:
        :return:
        """
        # validation
        if not string:
            return ""

        m, M = min(string, key=len), max(string, key=len)
        prefix = []

        for i in range(len(m)):
            if m[i] == M[i]:
                prefix.append(m[i])
            else:
                break
        return ''.join(prefix)


if __name__ == "__main__":
    prefix = Prefix()
    print(prefix.find_longest_common_prefix(["flower", "flow", "flowing"]))
