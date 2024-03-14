

class Binary:

    def count_substrings_with_01_combinations_v1(self, s: str) -> int:
        """
        Approach: Without array, using curr and prev
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        result, prev, curr = 0, 0, 1

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                # perform the count
                result += min(prev,curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return result + min(curr, prev)

    def count_substrings_with_01_combinations_v0(self, s: str) -> int:
        """
        Approach: Group Together using array
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        groups = [1]

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups.append(1)
            else:
                groups[-1] += 1

        result = 0

        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])
        return result


if __name__ == "__main__":
    binary = Binary()
    print(binary.count_substrings_with_01_combinations_v0("1010101"))
    print(binary.count_substrings_with_01_combinations_v0("101011"))
    print(binary.count_substrings_with_01_combinations_v0("10"))
    print(binary.count_substrings_with_01_combinations_v1("101011"))
    print(binary.count_substrings_with_01_combinations_v1("10"))