import pandas as pd
from typing import List


class CreateDataFrame:

    def create_data_frame(self, student_data: List[List[int]]) -> pd.DataFrame:
        """

        :param student_data:
        :return:
        """

        column_names = ['student_id', 'age']
        result_data_frame = pd.DataFrame(student_data, columns=column_names)
        return result_data_frame
