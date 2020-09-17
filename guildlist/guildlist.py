from bs4 import BeautifulSoup
import re
import requests
import time

time1 = time.time()
guild_page = requests.get('https://maple.gg/guild/elysium/%ED%9D%91%EB%AC%98/members?sort=level')
time2 = time.time()
soup = BeautifulSoup(guild_page.content, 'html.parser')
time3 = time.time()
guild_content = soup.find_all(class_ = 'col-lg-3 col-md-6 col-sm-6 mt-4')
time4 = time.time()
print(time4 - time3, time3 - time2, time2 - time1)
csv_mode = True

if(csv_mode):
    csv_file = open("guild_list.csv", "w")
    csv_file.write("닉네임,직업,레벨,최근 접속 일수,무릉층수,무릉시간\n")

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
    nick_soup = BeautifulSoup(webpage.content, "html.parser")
    floor = nick_soup.find(class_ = 'user-summary-floor font-weight-bold')
    floor_time = nick_soup.find(class_ = 'user-summary-duration')
    if(floor == None):
        floor = '-'
    else:
        floor = int(floor.get_text()[:-1])
    if(floor_time == None):
        floor_time = '-'
    else:
        floor_time = floor_time.get_text()
    
    if(csv_mode):
        csv_file.write(nickname+','+ job +','+ level +','+ last_summary_date +\
            ','+str(floor)+','+floor_time+'\n')
    time5 = time.time()
    
    