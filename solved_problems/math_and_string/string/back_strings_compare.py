

class BackStrings:

    def are_two_valid_v1(self, s: str, t: str) -> bool:
        """
        Approach: Two Pointers
        T: O(M * N)
        S: O(1)
        :param s:
        :param t:
        :return:
        """

        def find_valid_index(string: str, index: int) -> int:
            backspace_count = 0
            while index >= 0:
                if string[index] == "#":
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index

        p1, p2 = len(s) - 1, len(t) - 1

        while p1 >= 0 or p2 >= 0:

            p1 = find_valid_index(s, p1)
            p2 = find_valid_index(t, p2)

            # if they both became negative it is true
            # eg: s: a#b#c t: b#d#c -> c=c
            if p1 < 0 and p2 < 0:
                return True
            if p1 < 0 or p2 < 0 or s[p1] != t[p2]:
                return False
            p1 -= 1
            p2 -= 1
        # eg: s: a#dc t: a#bc -> ac=ac
        return True

    def are_two_valid_v0(self, s: str, t: str) -> bool:
        """
        T: O(M * N)
        S: O( M* N)
        :param s:
        :param t:
        :return:
        """
        def process_string(string: str):
            stack = []

            for char in string:
                if stack and char == "#":
                    stack.pop()
                else:
                    stack.append(char)
            return stack  # "".join(stack)

        p1 = process_string(s)
        p2 = process_string(t)

        # return p1 == p2

        if len(p1) != len(p2):
            return False

        for i in range(len(p1)):
            if p1[i] != p2[i]:
                return False
        return True


if __name__ == "__main__":
    back_strings = BackStrings()
    print(back_strings.are_two_valid_v0("a#bc", "a#dc"))
    print(back_strings.are_two_valid_v1("a#bc", "a#dc"))

    print(back_strings.are_two_valid_v0("#a#b#c", "#a#d#c"))
    print(back_strings.are_two_valid_v1("#a#b#c", "#a#b#c"))

    print(back_strings.are_two_valid_v0("#ab#s", "#ab#c"))
    print(back_strings.are_two_valid_v1("#ab#s", "#ab#c"))

    print(back_strings.are_two_valid_v0("a##bc", "a##dc"))
    print(back_strings.are_two_valid_v1("a##bc", "a##dc"))