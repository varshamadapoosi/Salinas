import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import pandas as pd

#maybe have a main url string variable
#and the course descriptions page string to add
#comes in handy in loop

URL = 'https://catalog.unh.edu/undergraduate/course-descriptions/'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = [] #array of all department links
for link in results:
	#note: this actually filters and gets relevant links
	#but it may not be the best for generalizing-->
	#is there a standard structure for department links?
	p =  re.search(r'\/undergraduate\/course-descriptions\/([^"]+)', str(link))
	#could possible do something with the first group?
	if p:
		departments.append("https://catalog.unh.edu" + p.group(0))
		##print(link.encode("utf-8"))
	
	#note: this extracts all links - may be useful for generalization
	#but not the best for getting most useful links for the page
	#print(link.get('href'))

#print(departments)

#now to the department: let's try one first
# department[4]: Agri Mech, departments[8] : Animal Science,
# department[248] : Sustainable Agri & Food systems
#same idea as before:
departments_of_interest = [departments[4], departments[8], departments[248]]
filename = "school_name" + ".csv"
	fn += 1
	csv_writer = csv.writer(open(filename, 'w'))
	csv_writer.writerow(["Title", "Credit", "Attr", "Desc"])
keywords = ["agri", "agricultural", "food", "animal"] # variations or no?
fn = 1
for dep in departments_of_interest:
	URL = dep
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	#how will classes differ across sites?
	courses = soup.findAll(class_="courseblock")
	for course in courses:
		title = course.find(class_="courseblocktitle").text
		check = course.findAll(class_="courseblockextra")
		attr = 'None'
		for c in check:
			if "Credit" in c.text:
				credit = c.text
			if "Attributes" in c.text:
				attr = c.text
	# this should work but it doesnt due to the error in the site page :c
	# desc = course.find(class_="courseblockdesc").text
	# if not desc: (this line doesn't work but should implement something like it)
		desc = re.search(r'(<\/p>)\n([^<]+)', str(course)).group(2)
		for key in keywords: #<-- filtered
			if (key in title or key in desc):
				csv_writer.writerow([title, credit, attr, desc])
	
	#csv_writer.writerow([title, credit, attr, desc]) <-- all
#csv_writer.close

#test = re.search(r'(<\/p>)\n([^<]+)', str(courses[0]))
#print(test.group(2))
