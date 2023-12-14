
# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)

# 셀레늄 임포트
import time as t
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# XPath 등을 통해 요소를 지목하기 위한 클래스
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True) # 브라우저를 끄지 않고 계속 유지를 시킬 수 있음.

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용할 수 있게 해주는 webdriver_manager의 기능.과 그 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 다운받은 크롬드라이버의 위치를 지정
# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴.
# driver =  webdriver.Chrome('C:/MyWork/chromedriver-win64/chromedriver.exe')
# driver =  webdriver.Chrome('C:/MyWork/chromedriver-win64/chromedriver.exe', options=option, service=service)
driver = webdriver.Chrome(options=option, service=service)


# 물리 드라이버로 사이트 이동 명령 get('URL')
driver.get('http://www.naver.com')

# 로딩되는 시간이 있을 수 있으므로 
t.sleep(1.5)

# 자동으로 버튼이나 링크 클릭 제어하기
# XPath -> XMl Path Language => 문서의 특정 요소나 속성에 접근하기 위한 경로로 지정하는 언어
# : 요소를 중복없이 정확하게 표현하기 쉬운 언어
login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a') # 찾은 이 요소를 리턴함
login_btn.click()

t.sleep(1)

# 자동으로 텍스트를 입력하기
id_input = driver.find_element(By.XPATH, '//*[@id="id"]')
id_input.send_keys('yoojin9199')

t.sleep(1)

driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys('aaa1234!')

t.sleep(1)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

