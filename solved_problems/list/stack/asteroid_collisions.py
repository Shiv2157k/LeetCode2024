from typing import List


class Asteroids:

    def without_collisions(self, asteroids: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param asteroids:
        :return:
        """

        stack = []

        for asteroid in asteroids:
            flag = True
            # if there are asteroids moving in opposite direction
            while stack and stack[-1] > 0 > asteroid:
                # case1: both will collide
                if stack[-1] < -1 * asteroid:
                    stack.pop()
                    continue
                # to handle cases like this [-2,-2,1,-2]
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                flag = False
                break
            if flag:
                stack.append(asteroid)
        return stack


if __name__ == "__main__":
    asteroids = Asteroids()
    print(asteroids.without_collisions([-2, -2, 1, -2]))
    print(asteroids.without_collisions([2, 10, -1, 2, -9]))
    print(asteroids.without_collisions([-10, 10]))
    print(asteroids.without_collisions([10, -10]))
    print(asteroids.without_collisions([10, 10]))
    print(asteroids.without_collisions([-10, -10]))
