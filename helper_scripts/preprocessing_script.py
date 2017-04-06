#
# Author: Derek Gorthy
# Date: 4/4/2017
# Description: Reduce file size and remove columns from csv
#
# Notes: Run with Python3 
#

import csv
import os



def add_line_to_file(line,output_file_name):
	with open(output_file_name, "a") as f:
		f.write(line)
	return



def remove_column(file_name, column_list, new_file_name):

	if(os.path.isfile(new_file_name)):
		os.remove(new_file_name)
	first_line = 1
	del_column_numbers = []

	f = open(file_name)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (first_line):
			first_line = 0
			column_number = 0
			
			for header in row:
				if header in column_list:
					del_column_numbers.append(column_number)
				column_number += 1

		for index in del_column_numbers:
			del row[index]

		init_str = ""

		for item in row:
			init_str = init_str + item + ","
		init_str = init_str[:-1] + "\n"

		add_line_to_file(init_str, new_file_name)

	return



remove_list = ['CurrentDataYear', 'RaceRecode3']

remove_column("../data/DeathRecords.csv", remove_list, "../data/DeathRecords_ver2.csv")