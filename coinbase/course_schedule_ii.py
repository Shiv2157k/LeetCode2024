from collections import deque
from typing import List


class GraphNode:
    def __init__(self):
        self.in_degree = 0
        self.out_nodes = []

class Schedule:
    """
        Always remember based on this problem
        To take course 0 you need to take course 1
        course |prerequisite
        [0     |        1]
        """
    # ToDo: DFS at least try to understand later
    def find_course_order(self, numOfCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Approach: Khans Algorithm
        T: O(M + N)
        S: O(M + N)
        :param numOfCourses:
        :param prerequisites:
        :return:
        """

        pre_req_map = {}

        for course, pre_req in prerequisites:
            pre_req_map[pre_req] = pre_req_map.get(pre_req, GraphNode())
            pre_req_map[pre_req].out_nodes.append(course)
            pre_req_map[course] = pre_req_map.get(course, GraphNode())
            pre_req_map[course].in_degree += 1

        queue = deque()

        for course in range(numOfCourses):
            if course not in pre_req_map:
                queue.append(course)
            elif pre_req_map[course].in_degree == 0:
                queue.append(course)

        course_order = []

        while queue:
            course = queue.popleft()
            course_order.append(course)
            if course in pre_req_map:
                for next_course in pre_req_map[course].out_nodes:
                    pre_req_map[next_course].in_degree -= 1
                    if pre_req_map[next_course].in_degree == 0:
                        queue.append(next_course)
        return course_order if len(course_order) == numOfCourses else []


if __name__ == "__main__":
    schedule = Schedule()
    print(schedule.find_course_order(
        5, [[1, 4], [2, 4], [3, 1], [3, 2]]
    ))

