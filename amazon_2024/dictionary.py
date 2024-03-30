from collections import defaultdict
from typing import List, Set


class UserWebSite:

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        Approach: HashMap + Sort
        T: O(N log N)
        S: O(n + m + n^3)
        :param username:
        :param timestamp:
        :param website:
        :return:
        """
        userToWebsiteMap = {}

        for user, ts, website in sorted(zip(username, timestamp, website), key=lambda x: (x[1], x[0])):
            userToWebsiteMap[user] = userToWebsiteMap.get(user, [])
            userToWebsiteMap[user].append(website)

        patternFreq = {}

        for user, websites in userToWebsiteMap.items():

            if len(websites) >= 3:
                comb = set()
                self._generateCombinations(websites, comb, [])

                for websitePattern in comb:
                    patternFreq[websitePattern] = patternFreq.get(websitePattern, 0) + 1

        maxPatternKey, maxFreq = None, float("-inf")

        for patternKey, freq in patternFreq.items():

            if freq > maxFreq:
                maxFreq = freq
                maxPatternKey = patternKey
            elif freq == maxFreq and patternKey < maxPatternKey:
                maxPatternKey = patternKey
        return list(maxPatternKey)

    def _generateCombinations(self, websites: List[str], combo: Set, combinations: List[str]):

        if len(combinations) == 3:
            t = tuple(combinations[:])
            if t not in combo:
                combo.add(t)
            return

        for index in range(len(websites)):
            self._generateCombinations(websites[index + 1:], combo, combinations + [websites[index]])


if __name__ == "__main__":
    userWebSite = UserWebSite()
    print(userWebSite.mostVisitedPattern(
        ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"],
        [436363475, 710406388, 386655081, 797150921],
        ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"]
    ))

    print(userWebSite.mostVisitedPattern(
        ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    ))
