from typing import List
from collections import deque


class GraphNode:

    def __init__(self):
        self.inDegree = 0
        self.outDegree = []


class CourseScheduleII:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Approach: Khans Topological Order
        T: O(M + N)
        S: O(M + N)
        :param numCourses:
        :param prerequisites:
        :return:
        """

        neighbors = {}
        queue = deque()

        for course, preReq in prerequisites:
            neighbors[preReq] = neighbors.get(preReq, GraphNode())
            neighbors[preReq].outDegree.appens(course)

            neighbors[course] = neighbors.get(course, GraphNode())
            neighbors[course].inDegree += 1

        for course in range(numCourses):
            if course in neighbors and neighbors[course].inDegre == 0:
                queue.append(course)
            elif course not in neighbors:
                queue.append(course)

        courseOrder = []

        while queue:
            course = queue.popleft()
            courseOrder.append(course)

            if course in neighbors:
                for nextCourse in neighbors[course].outDegree:
                    neighbors[nextCourse].inDegree -= 1
                    if neighbors[nextCourse].inDegree == 0:
                        queue.append(nextCourse)
        return courseOrder if len(courseOrder) == numCourses else []
           