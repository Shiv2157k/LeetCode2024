from typing import List
from pandas import DataFrame


class CreateDataFrame:

    def create(self, studentData: List[List[int]]) -> 'DataFrame':
        columnNames = ['student_id', 'age']
        resultDataFrane = DataFrame(studentData, columns=columnNames)
        return resultDataFrane


if __name__ == '__main__':
    cd = CreateDataFrame()
    print(cd.create(
        [
            [1, 15],
            [2, 11],
            [3, 11],
            [4, 20]
        ]
    ))
