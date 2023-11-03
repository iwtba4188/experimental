# 記得在requirements.txt裡面加上selenium跟webdriver-manager
# selenium==4.15.1
# webdriver-manager==3.4.2

import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

URL_PREFIX = "https://goodjob-nthu.conf.asia"
URL = URL_PREFIX + "/job_search.aspx"

# 無頭看要不要在 非developer 的情況下跑，或是要自己手動改也行
options = EdgeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()), options=options)
driver.get(URL)

try:
    WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, "wh")))
except TimeoutError:
    # 超時的情況暫時寫成這樣，挪到models裡面時再改
    print("TimeoutError")
    driver.close()
    exit()
else:
    page_num = len(driver.find_elements(By.CSS_SELECTOR, "input[type=submit]")) - 2

res = []
for i in range(0, page_num):
    try:
        # 顯式等待，等待class name為wh的元素出現
        WebDriverWait(driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wh")))
    except TimeoutError:
        # 超時的情況暫時寫成這樣，挪到models裡面時再改
        print("TimeoutError")
        driver.close()
        exit()
    else:
        driver.find_element(
            By.ID, f"ContentPlaceHolder1_UC_Pager1_RP_PG1_Button1_{i}").click()
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for job in soup.find_all("div", "articles"):
            j = {}
            j["job_detail_url"] = URL_PREFIX + job.div.a["href"]
            j["job_name"] = job.div.a.text
            j["job_area"] = job.select("span.label.span1")[0].text
            j["job_salary"] = job.select("span.label.span2")[0].text

            try:
                job_company = job.select("a.label")[0]
                job_company_url = URL_PREFIX + job_company["href"]
            except:
                job_company = job.select("p.label")[0]
                job_company_url = None

            j["job_company"] = job_company.text
            j["job_company_url"] = job_company_url
            j["job_time_period"] = job.select("span.label.span1")[1].text
            res.append(j)

driver.close()

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
