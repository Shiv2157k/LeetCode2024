class BuddyStrings:

    def isBuddy(self, s: str, goal: str) -> bool:
        """
        Approach: HashTable and Swap Check
        T: O(N)
        S: O(1)
        :param s:
        :param goal:
        :return:
        """

        # base validation
        if len(s) != len(goal):
            return False

        # Case 1: if both string and goal the same
        if s == goal:
            # only possibility to swap if we have repeated strings
            hashTable = [0] * 26
            for char in s:
                hashKey = ord(char) - ord('a')
                hashTable[hashKey] += 1
                if hashTable[hashKey] == 2:
                    return True
            return False

        # case 2: equal length but different characters
        # at most we can swap two of them so take two pointers
        firstPtr = -1
        secondPtr = -1

        for i in range(len(s)):

            if s[i] != goal[i]:
                # if they are not set let's set
                if firstPtr == -1:
                    firstPtr = i
                elif secondPtr == -1:
                    secondPtr = i
                else:  # it means we have a third character we cannot swap
                    # eg: s = abc, goal = def
                    return False

        # case 3: if it did not set then we have only one char
        # eg: s = abc, goal = dbc
        if secondPtr == -1:
            return False
        return s[firstPtr] == goal[secondPtr] and s[secondPtr] == goal[firstPtr]
