import requests
import json
from course import Course
from query_condition import Conditions


class CourseData:
    """可以添加 query 條件的課程資料。

    Attributes:
        course_data (``list[Course]``): 轉換為 Course 類別的課程資料。
    """

    NTHU_COURSE_DATA_URL = (
        "https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json"
    )

    def __init__(self) -> None:
        self.course_data = self._get_course_data()

    def _get_course_data(self) -> list[Course]:
        """TODO: error handler."""

        course_data_resp = requests.get(self.NTHU_COURSE_DATA_URL)
        course_data_text = course_data_resp.text

        course_data_dict_list = json.loads(course_data_text)
        course_data_format_list = list(map(Course, course_data_dict_list))

        return course_data_format_list

    def _get_course_data_by_json(self) -> list[Course]:
        # 使用 json 模組讀取檔案

        with open("course_data.json", "r", encoding="utf-8") as f:
            course_data_dict_list = json.load(f)

        return list(map(Course, course_data_dict_list))

    def query(self, conditions: Conditions) -> list[Course]:
        """搜尋所有符合條件的課程。

        Args:
            conditions (Conditions): 欲套用的條件式。

        Returns:
            list[Course]: 所有符合條件的課程。
        """

        res = []

        for course in self.course_data:
            if conditions.accept(course):
                res.append(course)

        return res
