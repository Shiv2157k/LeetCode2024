from collections import deque, defaultdict
from typing import List


class GraphNode:

    def __init__(self):
        self.in_degree = 0
        self.out_degree_nodes = []


class Course:
    """
    Always remember based on this problem
    To take course 0 you need to take course 1
    course |prerequisite
    [0     |        1]
    """

    def can_finish_v2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS
        T: O(M + N)
        S: O(M + N)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        pre_req_map = defaultdict(set)
        visited = set()

        for course, prerequisite in prerequisites:
            pre_req_map[course].add(prerequisite)

        def dfs(course: int) -> bool:
            if len(pre_req_map[course]) == 0 or course not in pre_req_map:
                return True
            if course in visited:
                return False

            visited.add(course)
            for next_course in pre_req_map[course]:
                if not dfs(next_course):
                    return False
            visited.pop()
            pre_req_map[course] = set()
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    def can_finish_v1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: Khans Algorithm for Topological Sorting with custom Graph DS
        T: O(M + N)
        S: O(M + N)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        pre_req_map = {}
        total_courses_depth = 0

        for course, prerequisite in prerequisites:
            pre_req_map[course] = pre_req_map.get(course, GraphNode())
            pre_req_map[course].out_degree_nodes.append(prerequisite)
            pre_req_map[prerequisite] = pre_req_map.get(prerequisite, GraphNode())
            pre_req_map[prerequisite].in_degree += 1
            total_courses_depth += 1

        queue = deque()

        for prerequisite, course in pre_req_map.items():
            if course.in_degree == 0:
                queue.append(prerequisite)

        curr_courses_depth = 0
        while queue:
            prerequisite = queue.popleft()
            for course in pre_req_map[prerequisite].out_degree_nodes:
                pre_req_map[course].in_degree -= 1
                curr_courses_depth += 1
                if pre_req_map[course].in_degree == 0:
                    queue.append(course)
        return total_courses_depth == curr_courses_depth

    def can_finish_v0(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach: Khans Algorithm for Topological Sorting
        T: O(M + N)
        S: O(M + N)
        :param numCourses:
        :param prerequisites:
        :return:
        """

        in_degree = [0] * numCourses
        pre_req_map = [[] for _ in range(numCourses)]

        # add the neighbors/ adjacent into the map
        for course, prerequisite in prerequisites:
            pre_req_map[prerequisite].append(course)
            in_degree[course] += 1

        queue = deque()
        # add the in-degree -> 0/ leaft nodes to queue
        # for 1st round of traversal
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        courses_completed = 0
        while queue:
            course = queue.popleft()
            courses_completed += 1
            for next_course in pre_req_map[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return courses_completed == numCourses


if __name__ == "__main__":
    subjects = Course()
    print(subjects.can_finish_v0(
        5, [[1, 4], [2, 4], [3, 1], [3, 2]]
    ))
    print(subjects.can_finish_v1(
        5, [[1, 4], [2, 4], [3, 1], [3, 2]]
    ))
