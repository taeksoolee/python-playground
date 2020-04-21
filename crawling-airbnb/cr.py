import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

'''
try:
    t = "https://www.airbnb.co.kr/rooms/7331795"
    req = requests.get(t)
    bsObject = BeautifulSoup(req.content, "html.parser")
    ##print(bsObject)
    f = open('foo.txt', 'w', encoding='UTF-8')
    f.write(str(bsObject))
    print(str(bsObject.find(id="details")))
    ##root = bsObject.find("div", {"id":"details"})
    ##spans = root.find_all("span", {"class":"_czm8crp"}
    ##print(spans)

    for root in roots:
        
        text = ""
        for span in spans:
            text += str(span.get("content"))
        print(text)
finally:
    f.close()
'''


driver = webdriver.Firefox()
driver.implicitly_wait(100)
driver.get('https://www.airbnb.co.kr/rooms/7331795')
'''
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print(soup.title)
details = soup.find("div", {"id", "details"})
print(details)
'''
###.get_attribute("textContent")
print(driver.find_element_by_id("details").get_attribute("textContent"))
##.find_all("span")