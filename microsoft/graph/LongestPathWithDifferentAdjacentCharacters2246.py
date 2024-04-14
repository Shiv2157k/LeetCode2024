from typing import List, Dict


class LongestPathWithDifferentAdjacentCharacters:

    def longestPath(self, parent: List[int], s: str):

        graph = {}
        result = 0

        for i in range(1, len(parent)):
            graph[i] = graph.get(i, [])
            graph[i].append(parent[i])

            graph[parent[i]] = graph.get(parent[i], [])
            graph[parent[i]].append(i)

        def dfs(currNode: int, parent: int):
            nonlocal result
            longest = 0
            secondLongest = 0

            for child in graph[currNode]:

                if child == parent:
                    continue

                childLongestLength = dfs(child, currNode)

                if s[child] == s[currNode]:
                    continue

                if childLongestLength > secondLongest:
                    secondLongest = childLongestLength

                if secondLongest > longest:
                    # swap
                    secondLongest, longest = longest, secondLongest

            LongestOrSecondLongestWithParent = max(longest, secondLongest) + 1
            justParent = 1
            parentLongestSecondLongest = 1 + longest + secondLongest

            result = max(result, LongestOrSecondLongestWithParent, justParent, parentLongestSecondLongest)

            return max(LongestOrSecondLongestWithParent, justParent)

        dfs( 0, -1)
        return result


if __name__ == "__main__":
    ll = LongestPathWithDifferentAdjacentCharacters()
    print(ll.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))
