from collections import deque
from typing import List
from math import ceil


class GraphNode:

    def __init__(self):
        self.inDegree = 0
        self.outDegree = []


class ReportsToCapital:

    def minFuelCostTookV1(self, roads: List[List[int]], seats: int) -> int:

        fuel = 0
        graph = {}

        for road in roads:

            graph[road[0]] = graph.get(road[0], GraphNode())
            graph[road[0]].outDegree.append(road[1])

            graph[road[1]] = graph.get(road[1], GraphNode())
            graph[road[1]].outDegree.append(road[0])

            graph[road[0]].inDegree += 1
            graph[road[1]].inDegree += 1


        queue = deque()
        totalNodes = len(roads) + 1

        for node in range(1, totalNodes):

            if graph[node].inDegree == 1:
                queue.append(node)

        representatives = [1] * totalNodes

        while queue:

            node = queue.popleft()

            fuel += ceil(representatives[node] / seats)

            for child in graph[node].outDegree:
                graph[child].inDegree -= 1
                representatives[child] += representatives[node]
                if graph[child].inDegree == 1:
                    queue.append(child)
        return fuel

    def minFuelCostTookV0(self, roads: List[List[int]], seats: int) -> int:

        fuel = 0
        # build the adjacent node
        adjacentNode = {}

        for road in roads:
            adjacentNode[road[0]] = adjacentNode.get(road[0], [])
            adjacentNode[road[0]].append(road[1])

            adjacentNode[road[1]] = adjacentNode.get(road[1], [])
            adjacentNode[road[1]].append(road[0])

        def depthFirstSearch(currNode: int, parent: int):
            nonlocal fuel
            representatives = 0
            # if there is no path b/w curr node & adjacent
            if currNode not in adjacentNode:
                return representatives

            for childNode in adjacentNode[currNode]:

                if childNode != parent:
                    representatives += depthFirstSearch(childNode, currNode)

            if currNode != 0:
                fuel += ceil(representatives / seats)
            return representatives

        depthFirstSearch(0, -1)

        return fuel
