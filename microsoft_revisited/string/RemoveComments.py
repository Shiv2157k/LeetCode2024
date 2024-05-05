from typing import List


class Comments:

    def remove(self, source: List[str]) -> List[str]:
        """
        Approach: As per the rules
        T: O(N * M)
        S: O(N)
        :param source:
        :return:
        """

        in_block = False
        output: List[str] = []

        for line in source:
            i = 0
            if not in_block:
                new_line: List[str] = []

            while i < len(line):

                if line[i: i + 2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i: i + 2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i: i + 2] == '//':
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            if new_line and not in_block:
                output.append(''.join(new_line))
        return output
