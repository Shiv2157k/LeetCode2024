from typing import List


class PalindromePartitioning:

    def partition(self, s: str) -> List[List[str]]:
        """
        Approach: Backtrack
        T: O(N * 2^N)
        S: O(N)
        :param s:
        :return:
        """
        result = []

        def back_track(start: int, path: List[str], sub_string: str):

            if start >= len(sub_string):
                result.append(list(path))
                return

            for end in range(start, len(sub_string)):
                if self._is_palindrome(sub_string, start, end):
                    path.append(s[start: end + 1])
                    back_track(end + 1, path, sub_string)
                    path.pop()

        back_track(0, [], s)
        return result

    def _is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
