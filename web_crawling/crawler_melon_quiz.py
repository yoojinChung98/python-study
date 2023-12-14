import time as t
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import traceback
import codecs

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(options=option, service=service)

driver.get('https://www.melon.com/chart/index.htm')

t.sleep(2)

d = datetime.today()
file_path = f'c:/test/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일.txt'

try:

    '''
    - with문을 사용하면 with 블록을 벗어나는 순간
     객체가 자동으로 해제됩니다. (자바의 try with resource와 비슷)

    - with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
    '''
    with codecs.open(file_path='w', encoding='utf-8') as f:
    # f = codecs.open(file_path, mode='w', encoding='utf-8')
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    song_list1 = soup.find_all('tr', class_='lst50')

    for song in song_list1:

        rank = song.select_one('div.t_center > span.rank').text
        title = song.select_one('div.rank01 a').text
        singer = song.select_one('div.rank02 a').text
        album = song.select_one('div.rank03 a').text

        f.write(f'# 순위: {rank}위\n')
        f.write(f'# 가수명: {singer}\n')
        f.write(f'# 앨범명: {album}\n')
        f.write(f'# 노래 제목: {title}\n')
        f.write('-'*4+'\n')
    
    song_list2 = soup.find_all('tr', class_='lst100')

    for song in song_list2:

        rank = song.select_one('div.t_center > span.rank').text
        title = song.select_one('div.rank01 a').text
        singer = song.select_one('div.rank02 a').text
        album = song.select_one('div.rank03 a').text

        f.write(f'# 순위: {rank}위\n')
        f.write(f'# 가수명: {singer}\n')
        f.write(f'# 앨범명: {album}\n')
        f.write(f'# 노래 제목: {title}\n')
        f.write('-'*4+'\n')

except: 
    print('파일 출력 실패!')
    print(traceback.format_exc())

finally:
    # f.close()
    pass


