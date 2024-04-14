from typing import List
from collections import deque


class GraphNode:

    def __init__(self):
        self.inDegree = 0
        self.outDegree = []


class CourseSchedule:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: Kahn's Topological Sort
        T: O(M + N)
        S: O(M + N)
        :param numCourses:
        :param prerequisites:
        :return:
        """

        graph = {}
        queue = deque()
        courseTaken = 0

        for course, preReq in prerequisites:
            graph[preReq] = graph.get(preReq, GraphNode())
            graph[preReq].outDegree.append(course)
            graph[course] = graph.get(course, GraphNode())
            graph[course].inDegree += 1

        for course in range(numCourses):
            if course in graph and graph[course].inDegree == 0:
                queue.append(course)
            elif course not in graph:
                queue.append(course)

        while queue:
            currCourse = queue.popleft()
            courseTaken += 1

            if currCourse not in graph:
                continue

            for nextCourse in graph[currCourse]:
                graph[nextCourse].inDegree -= 1
                if graph[nextCourse].inDegree == 0:
                    queue.append(nextCourse)
        return numCourses == courseTaken
