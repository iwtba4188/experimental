from course import Course
from constant import Field


class Condition:

    def __init__(self, type_: Field, value: str) -> None:
        self.type_ = type_.value
        self.value = value

    def check(self, course: Course) -> bool:
        return vars(course)[self.type_] == self.value


class Conditions:

    def __init__(self, type_: str, value: str) -> None:
        self.condition_stat = [Condition(type_, value), "and", True]
        self.course = None
        return

    def __and__(self, condition2):
        self.condition_stat = [self.condition_stat, "and", condition2.condition_stat]
        return self

    def __or__(self, condition2):
        self.condition_stat = [self.condition_stat, "or", condition2.condition_stat]
        return self

    def _solve_condition_stat(self, data: list) -> bool:
        lhs, op, rhs = data

        if type(lhs) == list:
            lhs = self.solve_condition_stat(lhs)
        elif type(lhs) == Condition:
            lhs = lhs.check(self.course)

        if type(rhs) == list:
            rhs = self.solve_condition_stat(rhs)
        elif type(rhs) == Condition:
            rhs = rhs.check(self.course)

        if op == "and":
            return (lhs and rhs)
        elif op == "or":
            return (lhs or rhs)

    def accept(self, course: Course) -> bool:
        self.course = course

        return self.solve_condition_stat(self.condition_stat)
