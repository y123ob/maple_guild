from bs4 import BeautifulSoup
from urllib import parse
import re
import requests
import time

guild_name = '흑묘'
guild_name_enc = parse.quote(guild_name)

time1 = time.time()
guild_page = requests.get('https://maple.gg/guild/elysium/{}/members?sort=level'.format(guild_name_enc))
time2 = time.time()
soup = BeautifulSoup(guild_page.content, 'html.parser')
time3 = time.time()
guild_content = soup.find_all(class_ = 'col-lg-3 col-md-6 col-sm-6 mt-4')
time4 = time.time()
print(time4 - time3, time3 - time2, time2 - time1)

csv_mode = True

if(csv_mode):
    csv_file = open('guild_list.csv', 'w')
    csv_file.write('닉네임,직업,레벨,최근 접속 일수,무릉층수,무릉시간\n')

for member in guild_content:
    nickname = member.find(class_ = re.compile('font-size-14 +')).get_text()
    job_level = member.find(class_ = 'font-size-12').get_text()
    last_summary_date = member.find(class_ = 'user-summary-date').get_text()
    job, level = job_level.split('/Lv.')
    job = job.replace(',' , '')
    last_summary_date = last_summary_date[9:-3]
    if(last_summary_date == '알'):
        last_summary_date = '-'
    
    nick_url = 'https://maple.gg/u/' + nickname
    webpage = requests.get(nick_url)
    nick_soup = BeautifulSoup(webpage.content, 'html.parser')

    floor_info = nick_soup.find_all(class_ = 'col-lg-3 col-6 mt-3 px-1')[0]
    no_floor_data = floor_info.find(class_ = 'user-summary-no-data')

    floor = '-'
    floor_time = '-'
    if no_floor_data == None:
        floor_value = floor_info.find(class_ = 'user-summary-floor font-weight-bold')
        if(floor_value != None):
            floor = int(floor_value.get_text()[:-1])

        floor_time_value = floor_info.find(class_ = 'user-summary-duration')
        if(floor_time_value != None):
            floor_time = floor_time_value.get_text()
    
    if(csv_mode):
        csv_file.write('{},{},{},{},{},{}\n'.format(nickname, job, level, last_summary_date, str(floor), floor_time))
    
    