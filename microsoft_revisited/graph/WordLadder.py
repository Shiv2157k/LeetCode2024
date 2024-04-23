from collections import deque
from typing import Dict, List, Deque


class WordLadder:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Approach: BFS
        T: O(M * N^2)
        S: O(M * N^2)
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """

        # validation
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        allComboDict = self._buildPossibleCombinations(wordList)
        # startNode, level
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}

        while queue:

            currWord, level = queue.popleft()
            # as all word length is same
            for i in range(len(beginWord)):
                intermediateWord = currWord[:i] + '*' + currWord[i + 1:]
                if intermediateWord in allComboDict:
                    for neighbor in allComboDict[intermediateWord]:
                        if neighbor == endWord:
                            return level + 1

                        if neighbor not in visited:
                            queue.append((neighbor, level + 1))
                            visited[neighbor] = True
                    # setting this to avoid cycle
                    allComboDict[intermediateWord] = []
        return 0

    def _buildPossibleCombinations(self, wordList: List[str]) -> Dict[str, List[str]]:
        allPossibleComboDict = {}
        for word in set(wordList):
            for i in range(len(word)):
                possibleWord = word[:i] + '*' + word[i + 1:]
                allPossibleComboDict[possibleWord] = allPossibleComboDict.get(possibleWord, [])
                allPossibleComboDict[possibleWord].append(word)
        return allPossibleComboDict
