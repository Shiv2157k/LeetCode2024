class RobotReturnToOrigin:

    def judge_circle(self, moves: str) -> bool:
        """
        Approach: Simulation
        T: O(N)
        S: O(1)
        :param moves:
        :return:
        """

        x: int = 0
        y: int = 0

        for move in moves:

            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        return x == y == 0
