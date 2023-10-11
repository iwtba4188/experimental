import re
from course import Course
from constant import Field


class Condition:

    def __init__(self, row_field: Field, matcher: str, regex_match: bool) -> None:
        self.row_field = row_field.value
        self.matcher = matcher
        self.regex_match = regex_match

    def check(self, course: Course) -> bool:
        course_data_dict = vars(course)
        field_data = course_data_dict[self.row_field]

        if self.regex_match == True:
            match_res = re.search(self.matcher, field_data)
            return False if match_res == None else True
        else:
            return field_data == self.matcher


class Conditions:

    def __init__(self, row_field: str, matcher: str | re.Pattern[str], regex_match: bool = False) -> None:
        self.condition_stat = [Condition(row_field, matcher, regex_match), "and", True]
        self.course = None

    def __and__(self, condition2):
        self.condition_stat = [self.condition_stat, "and", condition2.condition_stat]
        return self

    def __or__(self, condition2):
        self.condition_stat = [self.condition_stat, "or", condition2.condition_stat]
        return self

    def _solve_condition_stat(self, data: list) -> bool:
        lhs, op, rhs = data

        if type(lhs) == list:
            lhs = self._solve_condition_stat(lhs)
        elif type(lhs) == Condition:
            lhs = lhs.check(self.course)

        if type(rhs) == list:
            rhs = self._solve_condition_stat(rhs)
        elif type(rhs) == Condition:
            rhs = rhs.check(self.course)

        if op == "and":
            return (lhs and rhs)
        elif op == "or":
            return (lhs or rhs)

    def accept(self, course: Course) -> bool:
        self.course = course
        return self._solve_condition_stat(self.condition_stat)
