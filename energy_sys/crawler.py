import re
import requests
import json

URL_PREFIX = "http://140.114.188.57/nthu2020/fn1/kw"
URL_POSTFIX = ".aspx"

data_name = ["北區一號", "北區二號", "仙宮"]
json_data = []

for i in range(1, 4):
    res = requests.get(URL_PREFIX + str(i) + URL_POSTFIX)
    res_text = res.text

    data = re.search(r"alt=\"kW: ([\d,-]+?)\"", res_text, re.S).group(1)

    unit_json_data = {}
    unit_json_data["name"] = data_name[i-1]
    unit_json_data["data"] = data
    json_data.append(unit_json_data)

    print(data_name[i-1] + ": " + data + "kW")

with open("energy_sys.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
