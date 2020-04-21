import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

f = open("data.txt", "w", encoding="utf-8")
try:
    rex = re.compile('/room')

    list = []

    for i in range(0, 10):
        num = 0
        url = "https://www.airbnb.co.kr/s/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&source=mc_search_bar&search_type=pagination&screen_size=large&click_referer=t%3ASEE_ALL%7Csid%3A9d968e0d-3a2a-4246-bfc7-2808cab5d44f%7Cst%3AMAGAZINE_HOMES&title_type=MAGAZINE_HOMES&hide_dates_and_guests_filters=false&place_id=ChIJzWXFYYuifDUR64Pq5LTtioU&s_tag=dAhIfTyu&section_offset=4&items_offset="+str(num)
        req = requests.get(url)
        bsObject = BeautifulSoup(req.text, "html.parser")
        for link in bsObject.find_all('a'):
            data = str(link.get('href'))
            if rex.match(data):
                list.append("https://www.airbnb.co.kr"+str(str.split(data)[0]))
        num += 20

    ##print(list)
    print("start")

    ##driver = webdriver.Chrome()
    driver = webdriver.Firefox()

    driver.implicitly_wait(100)
    for ele in list:
        driver.get(ele)
        print(str(driver.find_element_by_id("details").get_attribute("textContent")))
        f.write(str(driver.find_element_by_id("details").get_attribute("textContent")))
        f.write("\n")
        print("complete")
finally:
    f.close()
    