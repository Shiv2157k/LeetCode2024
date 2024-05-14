class Celebrity:

    def knows(self, i, j) -> bool:
        return True

    def __init__(self):
        self.__number_of_people = 0

    def find_celebrity_v0(self, n: int):
        self.__number_of_people = n
        for p1 in range(n):
            if self._is_celebrity(p1):
                return p1
        return - 1

    def find_celebrity_v1(self, n: int):
        """
        Approach: Logical Deduction
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """
        self.__number_of_people = n
        celebrity = 0

        for i in range(1, self.__number_of_people):

            if self.knows(celebrity, i):
                celebrity = i

        if self._is_celebrity(celebrity):
            return celebrity
        return -1

    def _is_celebrity(self, p1):
        for p2 in range(self.__number_of_people):
            if p1 == p2:
                continue
            if self.knows(p1, p2) or not self.knows(p2, p1):
                return False
        return True
