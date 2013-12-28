# -*- coding: utf-8 -*-
import time
import sys

from bs4 import BeautifulSoup
import requests


if len(sys.argv) < 2:
    print("You need to provide a date in the format YYYY-MM-DD")
    sys.exit(1)

year, month, day = time.strptime(sys.argv[1], '%Y-%m-%d')[:3]

base_url = "http://www.wunderground.com/history/airport/SBRJ/{year}/{month}/{day}/DailyHistory.html"

url = base_url.format(year=year, month=month, day=day)

response = requests.get(url)
if response.status_code != 200:
    print("An error occurred while getting data for {day}/{month}/{year}".format(
        year=year, month=month, day=day))
    sys.exit(1)
else:
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find_all(attrs={'id': 'historyTable'})[0]
    mean_temp = int(table.tbody('tr')[1]('span')[2].text)

    print(mean_temp)
