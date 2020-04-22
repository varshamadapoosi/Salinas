import re
import csv

#the page divisors when copy pasting into txt
exclude = "LAC COURTE OREILLES"

keywords = ["agri\w+", "food", "animal"]
course_listings = []
titles = []
credits = []
descriptions = []
curr_desc = ""
with open(r"LAC_COURTE_OREILLES.txt", "r", encoding='utf-8', errors='ignore') as test:
	line = 0
	read = test.readlines()
	while line < len(read):
		# Title on one line
		t = re.search(r'(\w+\s\d{3})\s(\D+)(\d{1})\s(CR)', read[line], flags=re.IGNORECASE)
		if t:
			if curr_desc != "":
				descriptions += [curr_desc]
				curr_desc = ""
			course_listings += [t.group(1)]
			titles += [t.group(2)]
			credits += [t.group(3)]
		# Title on multiple lines
		# Ignoring the possible but unlikely case that the number stays on line but 'CR' goes to next line
		t_word = re.search(r'(\w+)\s(\d{3})\s(\D+)', read[line], flags=re.IGNORECASE)
		elif t_word:

			t_word_num = re.search(r'(\w+)\s(\d)\s(CR)', read[line + 1], flags=re.IGNORECASE):
			t_num =  re.search(r'(\d)\s(CR)', read[line + 1], flags=re.IGNORECASE):
			if t_word_num:
				# append to last line
			elif t_num:
				# set as credit
			line += 1
		else:
			if not exclude in read[line]:
				if 'Prerequisite' in read[line]:
					before = read[line].split('Prerequisite')[0]
					curr_desc += before
				else:
					curr_desc += read[line]
		line += 1
descriptions += [curr_desc]
filename = "LAC_COURTE_OREILLES.csv"
#csv_writer = csv.writer(open(filename, 'w'))
#csv_writer.writerow(["Course Listing", "Title", "Credit", "Desc"])
keywords = ["agri", "agricultural", "food", "animal"]

i = 0
test = []
while i < len(titles):
	for key in keywords:
		if (re.search(key, titles[i], flags=re.IGNORECASE) or 
			re.search(key, descriptions[i], flags=re.IGNORECASE)):
				test += [descriptions[i]]
			#csv_writer.writerow([course_listings[i], titles[i], credits[i], descriptions[i]])
	i += 1
print(test[0])
