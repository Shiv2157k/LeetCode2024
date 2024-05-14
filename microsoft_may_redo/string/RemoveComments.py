from typing import List


class RemoveComments:

    def remove_comments(self, source: List[str]) -> List[str]:
        """
        Approach: As per book rules
        T: O(N)
        S: O(1)
        :param source:
        :return:
        """

        in_block = False
        ans = []
        new_line = []

        for line in source:
            ptr = 0
            if not in_block:
                new_line = []

            while ptr < len(line):

                if line[ptr: ptr + 2] == '/*' and not in_block:
                    in_block = True
                    ptr += 1
                elif line[ptr: ptr + 2] == '*/' and in_block:
                    in_block = False
                    ptr += 1
                elif not in_block and line[ptr: ptr + 2] == '//':
                    break
                elif not in_block:
                    new_line.append(line[ptr])
                ptr += 1
            if new_line and not in_block:
                ans.append(''.join(new_line))
        return ans
