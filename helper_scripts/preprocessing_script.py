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


# Specific to 2014, can be made more extensible if needed
#
# Takes day_of_week: Int (Monday = 1, Tuesday = 2, ...)
#
def get_list_of_possible_dates(day_of_week, month):
	
	# Day of week on 1st, Number of days
	# Monday = 1
	date_data = [[3,31],[6,28],[6,31],[2,30],[4,31],[7,30],
					[2,31],[5,31],[1,30],[3,31],[6,30],[1,31]]

	possible_days = []
	cur_month = date_data[month-1]
	first_day = cur_month[0]

	if (day_of_week == first_day):
		possible_days.append(1)
	elif (day_of_week > first_day):
		possible_days.append(1+day_of_week-first_day)
	else:
		possible_days.append(8-(first_day-day_of_week))

	for date in range(possible_days[0]+7,cur_month[1],7):
		possible_days.append(date)

	return possible_days


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


def estimate_dates_from_day_of_week_uniform(input_file, output_file_name):

	return




# Used to remove redundant columns of data, can be used again if more found redundant
#remove_list = ['CurrentDataYear', 'RaceRecode3']
#remove_column("../data/DeathRecords.csv", remove_list, "../data/DeathRecords_ver2.csv")