import collections


class Letters:
    """
    Given a string s, remove duplicate letters so that every letter appears once and only once.
    You must make sure your result is the smallest in lexicographical order among all possible results.
    Example 1:
        Input: s = "bcabc"
        Output: "abc"
    Example 2:
        Input: s = "cbacdcbc"
        Output: "acdb"
    """

    def removeDuplicates(self, s: str) -> str:
        """
        Approach: Recursion
        Algorithm:
        - find the position of the left letter which is lesser
        - recursively remove the occurrences
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        pos = 0
        freq_map = collections.Counter(s)

        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            freq_map[s[i]] -= 1
            if freq_map[s[i]] == 0:
                break

        return s[pos] + self.removeDuplicates(s[pos:].replace(s[pos], '')) if s else ''

    def removeDuplicates1(self, s: str) -> str:
        """
        Approach: Using Stack
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        # to store the elements and perform comparison and pop recently pushed element
        stack = []
        # for the solution to track unique elements
        seen = set()
        # to track the previously occurred elements
        last_occurrence = {char: index for index, char in enumerate(s)}

        for index, char in enumerate(s):

            # if the character is not in the seen set
            if char not in seen:
                # 1. if stack contains chars
                # 2. current char is less than the top element in stack
                # 3. current index is less than last occurred index of that char
                while stack and stack[-1] > char and last_occurrence[stack[-1]] > index:
                    # we pop the stack and also remove the char from seen
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)


if __name__ == "__main__":
    letters = Letters()
    print(letters.removeDuplicates("bcabc"))
    print(letters.removeDuplicates("cbacdcbc"))
    print(letters.removeDuplicates1("bcabc"))
    print(letters.removeDuplicates1("cbacdcbc"))