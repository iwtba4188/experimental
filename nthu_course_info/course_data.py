import requests
import json
from course import Course
from query_condition import Conditions


class CourseData:

    NTHU_COURSE_DATA_URL = "https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json"

    def __init__(self) -> None:
        self.course_data = self._get_course_data()
        return

    def _get_course_data(self) -> list[Course]:
        course_data_resp = requests.get(self.NTHU_COURSE_DATA_URL)
        course_data_text = course_data_resp.text

        course_data_dict_list = json.loads(course_data_text)
        course_data_format_list = list(map(Course, course_data_dict_list))

        return course_data_format_list

    def query(self, conditions: Conditions) -> Course | None:
        res = []

        for course in self.course_data:
            if conditions.accept(course):
                res.append(course)

        return res
