

class Palindrome:

    def longest_palindrome(self, s: str) -> int:
        """
        Approach: Hash Table
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        occurrences = {}
        result = len(s)
        total_odd = 0

        for char in s:
            occurrences[char] = occurrences.get(char, 0) + 1

        for freq in occurrences.values():
            # calculate total odd
            if freq % 2 != 0:
                total_odd += 1

        if total_odd != 0:
            return result - total_odd + 1
        else:
            return result


if __name__ == "__main__":

    pal = Palindrome()
    print(pal.longest_palindrome("abccccdd")) # 7
    print(pal.longest_palindrome("abccccdddffgh"))  # 9
    print(pal.longest_palindrome("cc")) # 2
    print(pal.longest_palindrome("c")) # 1