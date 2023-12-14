
# DB에 저장

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By\

import mysql.connector

# DB접속을 위한 정보 세팅
mydb = mysql.connector.connect(
    host='localhost', # 포트번호는 mysqldb 라서 알아서 자동으로 붙는다고 함
    user='root',
    passwd='mysql',
    database='jpa',
)

# sql 실행을 위한 커서 생성
mycursor = mydb.cursor()

# user-agent 정보를 변환해주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

# User Agent 정보 변화 (필수 아님!) : 특정 브라우저를 차단하는 사이트가 가끔 있는데, 그러한 일을 해결하는 방법임.
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().edge)] # 헤더 정보를 edge로 변환 (내가 진입하는 사이트는 내가 edge 브라우저로 접근한 것으로 착각할 것.)
req.install_opener(opener) # 새로운 헤더 정보를 삽입



# 크롬 드라이버 구동 시 크롬 드라이버에게 전달할 옵션들 세팅
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# 브라우저 안뜨게 하기
# options.add_argument('--headless')
# 크롬 드라이버를 버전에 맞게 자동으로 지원해주는 객체
service = webdriver.ChromeService(ChromeDriverManager().install())

# 진짜 크롬 드라이버를 구동하는 코드
browser = webdriver.Chrome(service=service, options=options)

# 브라우저 사이즈 조정
browser.set_window_size(800, 600)

# 페이지 이동 (베스트셀러 페이지)
browser.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')


# 암묵적 대기: 웹 페이지 전체가 로딩 될 때까지 대기 후 남은 시간 무시.
browser.implicitly_wait(10)


cur_page_num = 2 # 현재 페이지 번호
target_page_num = 9 # 목적지 페이지 번호
rank = 1# 순위

while True:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    div_ss_book_box_list = soup.find_all('div', class_='ss_book_box')

    for div_ss_book_box in div_ss_book_box_list:


        # 타이틀, 작가, 가격정보를 모두 포함하는 ul부터 지목
        ul = div_ss_book_box.select_one('div.ss_book_list > ul')

        # 타이틀 
        title = ul.select_one('li > a.bo3')

        # 작가
        # 위에서 얻은 title의 부모요소 li의 다음 형제 li를 지목 -> 작가, 출판사, 출판일 존재.
        author = title.find_parent().find_next_sibling()

        # 작가쪽 영여 데이터 상세 분해
        author_data = author.text.split(' | ')
        authoer_name = author_data[0].strip() # strip(양쪽 공백 제거)
        company = author_data[1].strip() 
        pub_day = author_data[2].strip() 

        # 가격
        price = author.find_next_sibling()
        price_data = price.text.split(', ')[0]

        # sql을 문자열로 작성하고, 변수가 들어갈 위치를 %s로 표현합니다.
        # 값은 tuple로 순서대로 세팅해서 전달합니다.
        query = 'INSERT INTO tbl_crawling (data_rank, title, author, company, publish_date, price) VALUES(%s, %s, %s, %s, %s, %s)'
        values = (rank, title.text, authoer_name, company, pub_day, price_data)

        mycursor.execute(query, values)

        rank += 1


        
    # 다음 페이지(탭)로 전환
    cur_page_num += 1
    browser.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]/a').click()
    del soup # 뷰티풀수프객체 삭제: 다음페이지로 넘어갔으니 이제 안쓸거기도 하구, 어차피 반복문내에서 뷰티풀객체 또 생성될테니,, 정리해주는 것!
    browser.implicitly_wait(3)

    if cur_page_num == target_page_num:
        print('크롤링 종료!')
        break # while True break

    mydb.commit()
    # mydb.rollback() 예외 처리와 함께 사용해서, 중간에 에러 발생 시 기존의 insert 롤백 가능.

browser.close()
mycursor.close()
mydb.close()



