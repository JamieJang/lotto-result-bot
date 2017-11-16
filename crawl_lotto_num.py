import requests
from bs4 import BeautifulSoup as bs

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Botproject.settings')
import django
django.setup()
from lottoresult.models import ResultNumber

latest = 'http://www.nlotto.co.kr/gameResult.do?method=byWin'
url = 'http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo='

req = requests.get(latest)
html = req.content.decode('utf-8','replace')
soup = bs(html,'html.parser')
latest_round = soup.select(
	'#dwrNoList'
)
latest_round = latest_round[0].text.split('\n')[1]

for i in range( int(latest_round),0,-1 ):
	req = requests.get(url+str(i))
	html = req.content.decode('utf-8','replace')
	soup = bs(html,'html.parser')
	result = soup.select(
		'p.number > img'
	)
	result_nums = []
	for x in result:
		tmp = x.get('alt','')
		result_nums.append(tmp)

	ResultNumber.objects.update_or_create(rounds=str(i),result='-'.join(result_nums))

