from collections import deque
from typing import List


class GraphNode:

    def __init__(self):
        self.outDegree = []
        self.inDegree = 0


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

        neighbors = {}
        queue = deque()
        courseTaken = 0

        for course, preq in prerequisites:
            neighbors[preq] = neighbors.get(preq, GraphNode())
            neighbors[preq].outDeqgree.append(course)

            neighbors[course] = neighbors.get(course, GraphNode())
            neighbors[course].inDegree += 1

        for course in range(numCourses):

            if course in neighbors and neighbors[course].inDegree == 0:
                queue.append(course)
            elif course not in neighbors:
                queue.append(course)

        while queue:
            currCourse = queue.popleft()
            courseTaken += 1

            if currCourse not in neighbors:
                continue

            for nextCourse in neighbors[currCourse].outDegree:
                neighbors[nextCourse].inDegree -= 1
                if neighbors[nextCourse].inDegree == 0:
                    queue.append(nextCourse)
        return numCourses == courseTaken
