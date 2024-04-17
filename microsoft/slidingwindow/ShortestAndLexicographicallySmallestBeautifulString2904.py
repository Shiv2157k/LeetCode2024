from collections import deque

class ShortestBeautifulString:

    def get(self, s: str, k: int) -> str:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(N)
        :param s:
        :param k:
        :return:
        """

        onesIndexQueue = deque()
        ptr = 0
        result = ''

        while ptr < len(s):

            if s[ptr] == '1':
                onesIndexQueue.append(ptr)

            if len(onesIndexQueue) > k:
                onesIndexQueue.popleft()
            if len(onesIndexQueue) == k:
                currStr = s[onesIndexQueue[0]: onesIndexQueue[-1] + 1]

                if result == '' or len(currStr) < len(result):
                    result = currStr
                elif len(currStr) == len(result) and currStr < result:
                    result = currStr
            ptr += 1
        return result
