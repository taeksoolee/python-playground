from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

"""
# 모든 링크의 텍스트와 주소 가져오기
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
"""

"""
# 원하는 데이터의 content 내용을 가져옴
print (bsObject.head.find("meta", {"name":"description"}).get('content'))
"""

"""
# 원하는 데이터
print (bsObject.head.find("meta", {"name":"description"}))
"""


# 메타 데이터
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))


"""
# 타이틀
print(bsObject.head.title)
"""


"""
# 모든 데이터
print(bsObject)
"""
