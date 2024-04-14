from typing import List


class Comments:

    def remove(self, source: List[str]) -> List[str]:

        global newLine
        inBlock = False
        output = []

        for line in source:

            ptr = 0
            if not inBlock:
                newLine = []

            while ptr < len(line):

                # priority is /**/
                if line[ptr: ptr + 2] == "/*" and not inBlock:
                    inBlock = True
                    ptr += 1
                elif line[ptr: ptr + 2] == "*/" and inBlock:
                    inBlock = False
                    ptr += 1
                elif not inBlock and line[ptr: ptr + 2] == "//":
                    break
                elif not inBlock:
                    newLine.append(line[ptr])
                ptr += 1
            if newLine and not inBlock:
                output.append("".join(newLine))
        return output
