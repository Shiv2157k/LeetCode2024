

class Palindrome:

    def break_given(self, palindrome: str) -> str:
        """
        Approach: Greedy
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        length = len(palindrome)
        if length == 1:
            return ''

        for index in range(length // 2):

            if palindrome[index] != 'a':
                return palindrome[:index] + 'a' + palindrome[index + 1:]

        return palindrome[:-1] + 'b'


if __name__ == "__main__":

    pal = Palindrome()
    print(pal.break_given("a"))
    print(pal.break_given("aa"))
    print(pal.break_given("aba"))
    print(pal.break_given("ab"))
    print(pal.break_given("bab"))
