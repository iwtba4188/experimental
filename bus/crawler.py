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
towardSouthCampusInfo = re.search(
    r"const towardSouthCampusInfo = (\{.*?\})", res_text, re.S).group(1)
towardSouthCampusInfo = towardSouthCampusInfo.replace("\'", "\"")
towardSouthCampusInfo = towardSouthCampusInfo.replace(
    "direction", "\"direction\"")
towardSouthCampusInfo = towardSouthCampusInfo.replace(
    "duration", "\"duration\"")
towardSouthCampusInfo = towardSouthCampusInfo.replace("route", "\"route\"", 1)
towardSouthCampusInfo = towardSouthCampusInfo.replace("routeEN", "\"routeEN\"")
towardSouthCampusInfo = towardSouthCampusInfo.replace("\n", "")
# 往南大校區時刻表(平日)
weekdayBusScheduleTowardSouthCampus = re.search(
    r"const weekdayBusScheduleTowardSouthCampus = (\[.*?\])", res_text, re.S).group(1)
weekdayBusScheduleTowardSouthCampus = weekdayBusScheduleTowardSouthCampus.replace(
    "\'", "\"")
weekdayBusScheduleTowardSouthCampus = weekdayBusScheduleTowardSouthCampus.replace(
    "time", "\"time\"")
weekdayBusScheduleTowardSouthCampus = weekdayBusScheduleTowardSouthCampus.replace(
    "description", "\"description\"")
weekdayBusScheduleTowardSouthCampus = weekdayBusScheduleTowardSouthCampus.replace(
    "\n", "")
weekdayBusScheduleTowardSouthCampus = weekdayBusScheduleTowardSouthCampus.replace(
    ",    ]", "]")
# 往南大校區時刻表(假日)
weekendBusScheduleTowardSouthCampus = re.search(
    r"const weekendBusScheduleTowardSouthCampus = (\[.*?\])", res_text, re.S).group(1)
weekendBusScheduleTowardSouthCampus = weekendBusScheduleTowardSouthCampus.replace(
    "\'", "\"")
weekendBusScheduleTowardSouthCampus = weekendBusScheduleTowardSouthCampus.replace(
    "time", "\"time\"")
weekendBusScheduleTowardSouthCampus = weekendBusScheduleTowardSouthCampus.replace(
    "description", "\"description\"")
weekendBusScheduleTowardSouthCampus = weekendBusScheduleTowardSouthCampus.replace(
    "\n", "")
weekendBusScheduleTowardSouthCampus = weekendBusScheduleTowardSouthCampus.replace(
    ",    ]", "]")

# 往校本部資訊
towardMainCampusInfo = re.search(
    r"const towardMainCampusInfo = (\{.*?\})", res_text, re.S).group(1)
towardMainCampusInfo = towardMainCampusInfo.replace("\'", "\"")
towardMainCampusInfo = towardMainCampusInfo.replace(
    "direction", "\"direction\"")
towardMainCampusInfo = towardMainCampusInfo.replace("duration", "\"duration\"")
towardMainCampusInfo = towardMainCampusInfo.replace("route", "\"route\"", 1)
towardMainCampusInfo = towardMainCampusInfo.replace("routeEN", "\"routeEN\"")
towardMainCampusInfo = towardMainCampusInfo.replace("\n", "")
# 往校本部時刻表(平日)
weekdayBusScheduleTowardMainCampus = re.search(
    r"const weekdayBusScheduleTowardMainCampus = (\[.*?\])", res_text, re.S).group(1)
weekdayBusScheduleTowardMainCampus = weekdayBusScheduleTowardMainCampus.replace(
    "\'", "\"")
weekdayBusScheduleTowardMainCampus = weekdayBusScheduleTowardMainCampus.replace(
    "time", "\"time\"")
weekdayBusScheduleTowardMainCampus = weekdayBusScheduleTowardMainCampus.replace(
    "description", "\"description\"")
weekdayBusScheduleTowardMainCampus = weekdayBusScheduleTowardMainCampus.replace(
    "\n", "")
weekdayBusScheduleTowardMainCampus = weekdayBusScheduleTowardMainCampus.replace(
    ",    ]", "]")
# 往校本部時刻表(假日)
weekendBusScheduleTowardMainCampus = re.search(
    r"const weekendBusScheduleTowardMainCampus = (\[.*?\])", res_text, re.S).group(1)
weekendBusScheduleTowardMainCampus = weekendBusScheduleTowardMainCampus.replace(
    "\'", "\"")
weekendBusScheduleTowardMainCampus = weekendBusScheduleTowardMainCampus.replace(
    "time", "\"time\"")
weekendBusScheduleTowardMainCampus = weekendBusScheduleTowardMainCampus.replace(
    "description", "\"description\"")
weekendBusScheduleTowardMainCampus = weekendBusScheduleTowardMainCampus.replace(
    "\n", "")
weekendBusScheduleTowardMainCampus = weekendBusScheduleTowardMainCampus.replace(
    ",    ]", "]")


# 輸出 json 檔案
dataname = ["towardSouthCampusInfo", "weekdayBusScheduleTowardSouthCampus", "weekendBusScheduleTowardSouthCampus",
            "towardMainCampusInfo", "weekdayBusScheduleTowardMainCampus", "weekendBusScheduleTowardMainCampus"]
dataset = [towardSouthCampusInfo, weekdayBusScheduleTowardSouthCampus, weekendBusScheduleTowardSouthCampus,
           towardMainCampusInfo, weekdayBusScheduleTowardMainCampus, weekendBusScheduleTowardMainCampus]
for index, data in enumerate(dataset):
    print(data)
    j = json.loads(data)
    with open(f"{dataname[index]}.json", "w", encoding="utf-8") as f:
        json.dump(j, f, ensure_ascii=False, indent=4)
