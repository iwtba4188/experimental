import requests
import re
import json

URL = "https://ddfm.site.nthu.edu.tw/p/404-1494-256455.php?Lang=zh-tw"

res = requests.get(URL)
res_text = res.text

# 寫入檔案
with open("temp_res.txt", "w", encoding="utf-8") as f:
    f.write(res_text)

# 將字串轉換成 json 格式
restaurants_data = re.search(r"const restaurantsData = (\[.*?)  renderTabs", res_text, re.S).group(1)
restaurants_data = restaurants_data.replace("\'", "\"")
restaurants_data = restaurants_data.replace("\n", "")
restaurants_data = restaurants_data.replace(",  ]", "]")

# 輸出 json 檔案
with open("restaurants_data.json", "w", encoding="utf-8") as f:
    j = json.loads(restaurants_data)
    json.dump(j, f, ensure_ascii=False, indent=4)