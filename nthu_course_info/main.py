from course_data import CourseData
from query_condition import Conditions
from constant import Field

course_data = CourseData()


condition1 = Conditions(Field.CHINESE_TITLE, "文化人類學專題") & Conditions(Field.ID, "11210ANTH651000")
condition2 = Conditions(Field.CHINESE_TITLE, "化人類學專題") | Conditions(Field.ID, "11210ANTH651000")

condition_ce = Conditions(Field.LANGUAGE, "中") | Conditions(Field.LANGUAGE, "英")
condition_c = Conditions(Field.LANGUAGE, "中")
condition_e = Conditions(Field.LANGUAGE, "英")

print(condition1.condition_stat)

print("中文課名 與 ID (有一堂課): ", len(course_data.query(condition1)))
print(course_data.query(condition1))
print("中文課名 或 ID (有一堂課): ", len(course_data.query(condition2)))
print(course_data.query(condition2))

print()

print("總開課數: ", len(course_data.course_data))
print("中文授課 或 英文授課 開課數量: ", len(course_data.query(condition_ce)))
print("中文授課 開課數量: ", len(course_data.query(condition_c)))
print("英文授課 開課數量: ", len(course_data.query(condition_e)))
