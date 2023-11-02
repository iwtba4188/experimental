import requests
import re
import json

URL = "https://affairs.site.nthu.edu.tw/p/412-1165-20979.php?Lang=zh-tw"

res = requests.get(URL)
res_text = res.text

# 寫入檔案
with open("temp_res.txt", "w", encoding="utf-8") as f:
    f.write(res_text)

# 將字串轉換成 json 格式
# 往南大校區資訊
toward_south_campus_info = re.search(
    r"const towardSouthCampusInfo = (\{.*?\})", res_text, re.S).group(1)
toward_south_campus_info = toward_south_campus_info.replace("\'", "\"")
toward_south_campus_info = toward_south_campus_info.replace(
    "direction", "\"direction\"")
toward_south_campus_info = toward_south_campus_info.replace(
    "duration", "\"duration\"")
toward_south_campus_info = toward_south_campus_info.replace(
    "route", "\"route\"", 1)
toward_south_campus_info = toward_south_campus_info.replace(
    "routeEN", "\"routeEN\"")
toward_south_campus_info = toward_south_campus_info.replace("\n", "")
# 往南大校區時刻表(平日)
weekday_bus_schedule_toward_south_campus = re.search(
    r"const weekdayBusScheduleTowardSouthCampus = (\[.*?\])", res_text, re.S).group(1)
weekday_bus_schedule_toward_south_campus = weekday_bus_schedule_toward_south_campus.replace(
    "\'", "\"")
weekday_bus_schedule_toward_south_campus = weekday_bus_schedule_toward_south_campus.replace(
    "time", "\"time\"")
weekday_bus_schedule_toward_south_campus = weekday_bus_schedule_toward_south_campus.replace(
    "description", "\"description\"")
weekday_bus_schedule_toward_south_campus = weekday_bus_schedule_toward_south_campus.replace(
    "\n", "")
weekday_bus_schedule_toward_south_campus = weekday_bus_schedule_toward_south_campus.replace(
    ",    ]", "]")
# 往南大校區時刻表(假日)
weekend_bus_schedule_toward_south_campus = re.search(
    r"const weekendBusScheduleTowardSouthCampus = (\[.*?\])", res_text, re.S).group(1)
weekend_bus_schedule_toward_south_campus = weekend_bus_schedule_toward_south_campus.replace(
    "\'", "\"")
weekend_bus_schedule_toward_south_campus = weekend_bus_schedule_toward_south_campus.replace(
    "time", "\"time\"")
weekend_bus_schedule_toward_south_campus = weekend_bus_schedule_toward_south_campus.replace(
    "description", "\"description\"")
weekend_bus_schedule_toward_south_campus = weekend_bus_schedule_toward_south_campus.replace(
    "\n", "")
weekend_bus_schedule_toward_south_campus = weekend_bus_schedule_toward_south_campus.replace(
    ",    ]", "]")

# 往校本部資訊
toward_main_campus_info = re.search(
    r"const towardMainCampusInfo = (\{.*?\})", res_text, re.S).group(1)
toward_main_campus_info = toward_main_campus_info.replace("\'", "\"")
toward_main_campus_info = toward_main_campus_info.replace(
    "direction", "\"direction\"")
toward_main_campus_info = toward_main_campus_info.replace(
    "duration", "\"duration\"")
toward_main_campus_info = toward_main_campus_info.replace(
    "route", "\"route\"", 1)
toward_main_campus_info = toward_main_campus_info.replace(
    "routeEN", "\"routeEN\"")
toward_main_campus_info = toward_main_campus_info.replace("\n", "")
# 往校本部時刻表(平日)
weekday_bus_schedule_toward_main_campus = re.search(
    r"const weekdayBusScheduleTowardMainCampus = (\[.*?\])", res_text, re.S).group(1)
weekday_bus_schedule_toward_main_campus = weekday_bus_schedule_toward_main_campus.replace(
    "\'", "\"")
weekday_bus_schedule_toward_main_campus = weekday_bus_schedule_toward_main_campus.replace(
    "time", "\"time\"")
weekday_bus_schedule_toward_main_campus = weekday_bus_schedule_toward_main_campus.replace(
    "description", "\"description\"")
weekday_bus_schedule_toward_main_campus = weekday_bus_schedule_toward_main_campus.replace(
    "\n", "")
weekday_bus_schedule_toward_main_campus = weekday_bus_schedule_toward_main_campus.replace(
    ",    ]", "]")
# 往校本部時刻表(假日)
weekend_bus_schedule_toward_main_campus = re.search(
    r"const weekendBusScheduleTowardMainCampus = (\[.*?\])", res_text, re.S).group(1)
weekend_bus_schedule_toward_main_campus = weekend_bus_schedule_toward_main_campus.replace(
    "\'", "\"")
weekend_bus_schedule_toward_main_campus = weekend_bus_schedule_toward_main_campus.replace(
    "time", "\"time\"")
weekend_bus_schedule_toward_main_campus = weekend_bus_schedule_toward_main_campus.replace(
    "description", "\"description\"")
weekend_bus_schedule_toward_main_campus = weekend_bus_schedule_toward_main_campus.replace(
    "\n", "")
weekend_bus_schedule_toward_main_campus = weekend_bus_schedule_toward_main_campus.replace(
    ",    ]", "]")


# 輸出 json 檔案
dataname = ["toward_south_campus_info", "weekday_bus_schedule_toward_south_campus", "weekend_bus_schedule_toward_south_campus",
            "toward_main_campus_info", "weekday_bus_schedule_toward_main_campus", "weekend_bus_schedule_toward_main_campus"]
dataset = [toward_south_campus_info, weekday_bus_schedule_toward_south_campus, weekend_bus_schedule_toward_south_campus,
           toward_main_campus_info, weekday_bus_schedule_toward_main_campus, weekend_bus_schedule_toward_main_campus]
for index, data in enumerate(dataset):
    print(data)
    j = json.loads(data)
    with open(f"{dataname[index]}.json", "w", encoding="utf-8") as f:
        json.dump(j, f, ensure_ascii=False, indent=4)
