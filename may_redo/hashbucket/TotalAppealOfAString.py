class TotalAppealOfAString:

    def appeal_sum(self, s: str) -> int:
        """
        Approach: Hash Bucket with index of letter
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        total_appeal = 0
        curr_sum = 0
        occurrence_bucket = [-1] * 26

        for index, char in enumerate(s):
            bucket_key = ord('char') - ord('a')
            curr_sum += index - occurrence_bucket[bucket_key]
            total_appeal += curr_sum
            occurrence_bucket[bucket_key] = index
        return total_appeal
