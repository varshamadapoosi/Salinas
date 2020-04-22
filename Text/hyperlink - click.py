import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import pandas as pd

URL = 'http://catalog.umb.edu/preview_course_nopop.php?catoid=28&coid=171149'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find(class_='block_content')
breaks = results.findAll('em')
#print(results.encode("utf-8"))
for b in breaks:
	print(b.encode("utf-8"))
	# desc = course.find(class_="courseblockdesc").text
	# desc = re.search(r'(<\/p>)\n([^<]+)', str(course)).group(2)
