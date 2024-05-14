class FoodBucketsToFeedHamsters:

    def minimum_food_buckets(self, hamsters: str) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param hamsters:
        :return:
        """

        bucket_count = 0
        pointer = 0
        length = len(hamsters)

        while pointer < length:

            if hamsters[pointer] == 'H':

                # case 1: always add a bucket on to right if there is space
                if pointer + 1 < length and hamsters[pointer + 1] == '.':
                    bucket_count += 1
                    pointer += 2
                # case 2: no buckets on the left then add there is space
                elif pointer > 0 and hamsters[pointer - 1] == '.':
                    bucket_count += 1
                else:  # no space to place a bucket
                    return -1
            pointer += 1
        return bucket_count
