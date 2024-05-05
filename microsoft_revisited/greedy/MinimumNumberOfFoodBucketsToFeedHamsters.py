from typing import List


class Hamsters:

    def minimum_number_of_food_buckets(self, hamsters: str):
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param hamsters:
        :return:
        """

        bucket_count: int = 0
        pointer: int = 0
        length: int = len(hamsters)

        while pointer < length:

            if hamsters[pointer] == 'H':

                # case 1: always place bucket right side of hamster hoping the next hamster gets fed
                if pointer + 1 < length and hamsters[pointer + 1] == '.':
                    pointer += 2
                    bucket_count += 1
                # case 2: if we have reached here that means bucket is not reachable for the next hamster
                # so place it to its left or this hamster is located rightmost
                elif pointer > 0 and hamsters[pointer - 1] == '.':
                    bucket_count += 1
                else:  # case 3: there is no space to place the bucket
                    return -1
            pointer += 1
        return bucket_count
