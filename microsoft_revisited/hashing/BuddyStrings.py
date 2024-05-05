from typing import List


class BuddyStrings:

    def are_buddies(self, s: str, goal: str) -> bool:
        """
        Approach: Hash bucket
        T: O(N)
        S: O(26) -> 26 is constant
        :param s:
        :param goal:
        :return:
        """

        # validation
        if len(s) != len(goal):
            return False

        # case 1: same strings
        if s == goal:
            hash_bucket = [0] * 26
            for char in s:
                hash_key = ord(char) - ord('a')
                hash_bucket[hash_key] += 1
                if hash_bucket[hash_key] == 2:
                    return True
            return False

        # case 2: same length but different letters
        ptr1 = -1
        ptr2 = -1

        for i in range(len(s)):

            if s[i] != goal[i]:

                if ptr1 == -1:
                    ptr1 = i
                elif ptr2 == -1:
                    ptr2 = i
                else:
                    return False

        if ptr2 == -1:
            return False

        return s[ptr1] == goal[ptr2] and s[ptr2] == goal[ptr1]
