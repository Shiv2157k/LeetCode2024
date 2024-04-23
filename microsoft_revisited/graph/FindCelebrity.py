class API:

    def knows(self, x: int, y: int) -> bool:
        return x == y


class Celebrity:
    total_people: int = 0

    def findCelebrity(self, n: int) -> int:

        self.total_people = n
        celebrity_person = 0

        for i in range(1, self.total_people):

            if API.knows(celebrity_person, i):
                celebrity_person = i

        if self._is_celebrity(celebrity_person):
            return celebrity_person
        return -1

    def _is_celebrity(self, i: int) -> bool:
        for j in range(self.total_people):
            if i == j:
                continue
            if API.knows(i, j) or not API.knows(j, i):
                return False
        return True
