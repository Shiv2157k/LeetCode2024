from string import ascii_lowercase


class AdjacentString:

    def remove_all_v1(self, s: str) -> str:
        """
        Approach: Stack
        T: O(N)
        S: O(N - D)
        :param s:
        :return:
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    def remove_all_v0(self, s: str) -> str:
        """
        Brute Force
        T: O(N^2)
        S: O(N)
        :param s:
        :return:
        """
        duplicates = {ch * 2 for ch in ascii_lowercase}
        prev_length = -1

        while prev_length != len(s):
            prev_length = len(s)
            for duplicate in duplicates:
                s = s.replace(duplicate, '')
        return s


if __name__ == "__main__":
    strings = AdjacentString()
    print(strings.remove_all_v0("aabccbcde"))
    print(strings.remove_all_v1("aabccbcde"))
