from typing import List, Set
from collections import deque, defaultdict


class WordLadderII:

    def __init__(self):
        self.adjList = defaultdict(list)
        self.currPath = []
        self.shortestPaths = []

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)
        self._breadthFirstSearch(beginWord, wordSet)

        self.currPath.append(endWord)
        self._backtrack(endWord, beginWord)
        return self.shortestPaths

    def _buildNeighbors(self, word: str, wordList: Set[str]) -> List[str]:
        neighbors = []
        charList = list(word)

        for i in range(len(word)):
            oldChar = charList[i]
            for c in range(ord('a'), ord('z') + 1):
                charList[i] = chr(c)
                if charList[i] != oldChar and ''.join(charList) in wordList:
                    neighbors.append(''.join(charList))
            charList[i] = oldChar
        return neighbors

    def _backtrack(self, source: str, destination: str) -> None:

        if source == destination:
            self.shortestPaths.append(self.currPath[::-1])

        if source not in self.adjList:
            return

        if source in self.adjList:
            for word in self.adjList[source]:
                self.currPath.append(word)
                self._backtrack(word, destination)
                self.currPath.pop()

    def _breadthFirstSearch(self, beginWord: str, wordList: Set[str]) -> None:

        queue = deque([beginWord])
        wordList.discard(beginWord)

        isEnqueued = {beginWord: 1}

        while queue:
            visited = []

            for _ in range(len(queue)):

                currWord = queue.popleft()
                neighbors = self._buildNeighbors(currWord, wordList)

                for word in neighbors:
                    visited.append(word)
                    self.adjList[word].append(currWord)
                    if word not in isEnqueued:
                        queue.append(word)
                        isEnqueued[word] = 1
            for word in visited:
                wordList.discard(word)
