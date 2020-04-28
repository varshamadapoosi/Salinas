import re
import csv

course_listings = []
titles = []
credits = []
descriptions = []
curr_desc = ""

def parse(txt_file, title_pattern, 
	pattern_no_cred, pattern_cont1, pattern_cont2,
	c_l_group, t_group, c_group, prereqBefore):
	"""Takes in a string TXT_FILE indicating the name of txt
	 file to parse. Utilizes a regex TITLE_PATTERN to separate title
	 and data."""
	global descriptions
	with open(txt_file, "r", encoding='utf-8', errors='ignore') as text:
		line = 0
		read = text.readlines()
		while line < len(read):
			# Title on one line
			t = re.search(title_pattern, read[line], flags=re.IGNORECASE)
			# Title on multiple lines
			t_cut = re.search(pattern_no_cred, read[line], flags=re.IGNORECASE)
			if t:
				input_info(c_l_group, t_group, c_group)
			elif t_cut:
				t_word_num = re.search(pattern_cont1, read[line + 1], flags=re.IGNORECASE)
				t_num = re.search(pattern_cont2, read[line + 1], flags=re.IGNORECASE)
				if t_word_num:
					input_info(c_l_group, t_word.group(2) + t_word_num.group(1), 
								t_word_num.group(2))
				elif t_num:
					input_info(c_l_group, t_word.group(2), t_num.group(1))
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

def input_info(c_l_group, t_group, c_group):
	"""Takes in strings and adds to respective lists."""
	global course_listings
	global titles
	global credits
	global descriptions
	global curr_desc
	if curr_desc != ""
		descriptions += [curr_desc]
		curr_desc = ""
	course_listings += [c_l_group]
	titles += [t_group]
	credits += [c_group]

def write_to_csv(school_name):
	"""Filters parsed data to only include courses that contain
	keywords and writes these courses into a csv file named SCHOOL_NAME."""
	filename = school_name + ".csv"
	csv_writer = csv.writer(open(filename, 'w'))
	csv_writer.writerow(["Course Listing", "Title", "Credit", "Desc"])
	keywords = ["agri\w+", "food", "animal"] 
	# replace with import_keys for full list
	i = 0
	while i < len(titles):
		for key in keywords:
			if (re.search(key, titles[i], flags=re.IGNORECASE) or
				re.search(key, descriptions[i], flags=re.IGNORECASE)):
				csv_writer.writerow([course_listings[i], titles[i], credits[i], descriptions[i]])


def import_keys():
	"""Returns a list of all keywords in the keyword.txt file in cwd."""
	with open(r"keywords.txt", "r") as lines:
		for line in lines:
			if (line != "\n"):
				if "\n" in line:
					line = line.split("\n")[0]
				keywords += [line]
	return keywords