class TotalAppealOfAString:

    def appeal_sum(self, s: str) -> int:
        """
        Approach: HashBucket with index as values
        T: O(N)
        S: O(1) -> constant space
        :param s:
        :return:
        """

        curr_sum = 0
        total_sum = 0
        last_occurrence_bucket = [-1] * 26

        for index, char in enumerate(s):
            bucket_key = ord(char) - ord('a')

            curr_sum += index - last_occurrence_bucket[bucket_key]
            total_sum += curr_sum

            last_occurrence_bucket[bucket_key] = index
        return total_sum
