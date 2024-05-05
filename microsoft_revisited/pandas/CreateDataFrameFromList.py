from typing import List
import pandas as pd


class DataFrame:

    def create(self, student_data: List[List[int]]) -> pd.DataFrame:
        column_names = ['student_id', 'age']
        result_data_frame = pd.DataFrame(student_data, columns=column_names)
        return result_data_frame
