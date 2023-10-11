import re
from course import Course
from constant import Field


class Condition:
    """利用資訊確認 query 是否成功的最小單位。

    比對課程資料的欄位，確認是否滿足設定的配對（match）條件，可使用全等比對或正則表達式。

    Attributes:
        row_field(``ENUM.Field``): 用以指定要配對的欄位。
        matcher(``str``): 判斷式。
        regex_match(``bool``): 當 ``True`` 時將 matcher 視為正則表達式，反之視為普通字串並使用全等比對。
    """

    def __init__(self, row_field: Field, matcher: str, regex_match: bool) -> None:
        self.row_field = row_field.value
        self.matcher = matcher
        self.regex_match = regex_match

    def check(self, course: Course) -> bool:
        """ 確認是否滿足判斷式。 """

        course_data_dict = vars(course)
        field_data = course_data_dict[self.row_field]

        if self.regex_match == True:
            match_res = re.search(self.matcher, field_data)
            return False if match_res == None else True
        else:
            return field_data == self.matcher


class Conditions:
    """包裝 Condition 類別，組合成特別的結構以處理條件之 AND 、 OR 邏輯。

    將條件邏輯包裝進 list，模擬不同條件間 AND 、 OR 的邏輯組合。初始化參數與 Condition 相同，是傳遞參數的角色。

    Attributes:
        condition_stat(``list[Condition | str | bool]``): 特定結構模擬出的表達式格式。
        course(``Course``): 當前套用條件的課程。
    """

    def __init__(self, row_field: str, matcher: str | re.Pattern[str], regex_match: bool = False) -> None:
        self.condition_stat = [Condition(row_field, matcher, regex_match), "and", True]
        self.course = None

    def __and__(self, condition2):
        """ Override bitwise ``and`` operator 當成 logical ``and``。 """

        self.condition_stat = [self.condition_stat, "and", condition2.condition_stat]
        return self

    def __or__(self, condition2):
        """ Override bitwise ``or`` operator 當成 logical ``or``。 """

        self.condition_stat = [self.condition_stat, "or", condition2.condition_stat]
        return self

    def _solve_condition_stat(self, data: list) -> bool:
        """ 遞迴函式，拆分成 左手邊、運算子、右手邊，將左右手遞迴解成 ``bool`` 之後，再算出這一層的結果。 """

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
        """ 包裝遞迴函式供外部使用，回傳以該課程計算多個條件運算後的結果。 """

        self.course = course
        return self._solve_condition_stat(self.condition_stat)
