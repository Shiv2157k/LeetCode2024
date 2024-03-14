

class Subsequence:

    def smallest_of_distinct_chars(self, s: str):
        """
        Approach: Stacks and Set
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        stack, seen = [], set()

        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        for char in s:
            freq_map[char] -= 1
            if char not in seen:
                while stack and stack[-1] > char and freq_map[stack[-1]] != 0:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)


if __name__ == "__main__":
    string = Subsequence()
    print(string.smallest_of_distinct_chars("ababacded"))
    print(string.smallest_of_distinct_chars("fababd"))
    print(string.smallest_of_distinct_chars("gfa"))
    print(string.smallest_of_distinct_chars("dafbbfsxzdac"))