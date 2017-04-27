#
# Author: Derek Gorthy
# Date: 4/4/2017
# Description: Reduce file size and remove columns from csv
#
# Notes: Run with Python3 
#

import csv
import os
import random


MAX_FILE_SIZE_LIMIT_WITH_ROOM = 5000000


def add_line_to_file(row,output_file_name):

	init_str = ""
	for item in row:
		init_str = init_str + item.strip('\t') + ","
	init_str = init_str[:-1] + "\n"

	with open(output_file_name, "a") as f:
		f.write(init_str)
	return


# Month must be called: MonthOfDeath
# Day must be called: DayOfDeath
#
# Function will still return None if either of these columns are not found
# Returns [int_month, int_day] normally
#
def get_month_and_day_indeces(input_file):

	return_array = [0,0]

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		for i in range(0, len(row)):
			if (row[i] == "MonthOfDeath"):
				return_array[0] = i
			elif (row[i] == "DayOfDeath"):
				return_array[1] = i 
		if (return_array[0] == 0 or return_array[1] == 0):
			return None
		return return_array


# Format: [[data],[data],...]
#
def return_file_as_array(input_file, column_header_in_file):

	first_line = column_header_in_file
	return_array = []

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (first_line):
			first_line = 0
			
		else:
			return_array.append(row)

	return return_array


# Format: [[data],[data],...]
#
def return_file_as_dict(input_file, column_header_in_file):

	first_line = column_header_in_file
	return_dict = {}

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (first_line):
			first_line = 0
			
		else:
			init_str = str(row[0]) + "," + str(row[1])
			return_dict[init_str] = row[2]

	return return_dict


# Specific to 2014, can be made more extensible if needed
#
# Takes day_of_week: Int (Monday = 1, Tuesday = 2, ...)
#
def get_list_of_possible_days(day_of_week, month):
	
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

		add_line_to_file(row, new_file_name)

	return


def estimate_dates_from_day_of_week_uniform(input_file, row_to_insert, output_file):

	counter = 0
	if(os.path.isfile(output_file)):
		os.remove(output_file)
	first_line = 1

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (counter%1000 == 0):
			print("Line: ", counter)

		if (first_line):
			first_line = 0
			row.insert(row_to_insert,"Day")
			
		else:
			possible_days = get_list_of_possible_days(int(row[16]),int(row[5]))
			estimated_day = random.choice(possible_days)
			row.insert(row_to_insert,str(estimated_day))

		add_line_to_file(row, output_file)
		counter += 1

	return

# Takes a file that can have a header, user must specify a 
# If a day is listed, a 1 will be added, otherwise a 0 will be added
# Will insert new data into the last row
#
def add_data_binary(input_file, supplementary_file, column_header_in_supplementary, new_heading, output_file):

	counter = 0
	first_line = 1
	row_to_insert = 0
	true_array = return_file_as_array(supplementary_file,column_header_in_supplementary)
	month_day_array = get_month_and_day_indeces(input_file)
	month_index = month_day_array[0]
	day_index = month_day_array[1]

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (counter%100000 == 0):
			print("Line: ", counter)
		if (first_line):
			row_to_insert = len(row)
			first_line = 0
			row.insert(row_to_insert,new_heading)
		else:
			row.insert(row_to_insert,str([row[month_index],row[day_index]] in true_array))

		add_line_to_file(row,output_file)
		counter += 1

	return


# Supplementary file must be formatted like: month, day, data
#
def add_daily_data(input_file, supplementary_file, column_header_in_supplementary, not_found_str, new_heading, output_file):

	counter = 0
	first_line = 1
	row_to_insert = 0
	supplementary_dict = return_file_as_dict(supplementary_file,column_header_in_supplementary)
	month_day_array = get_month_and_day_indeces(input_file)
	month_index = month_day_array[0]
	day_index = month_day_array[1]

	f = open(input_file)
	csv_f = csv.reader(f)

	for row in csv_f:
		if (counter%100000 == 0):
			print("Line: ", counter)
		if (first_line):
			row_to_insert = len(row)
			first_line = 0
			row.insert(row_to_insert,new_heading)
		else:
			init_str = str(row[month_index]) + "," + str(row[day_index])
			if (init_str in supplementary_dict):
				row.insert(row_to_insert, supplementary_dict[init_str])
			else:
				row.insert(row_to_insert, not_found_str)

		add_line_to_file(row, output_file)
		counter += 1

	return


# Takes output_dir --> ../some_dir/
#
def break_large_file(input_file, output_dir):

	file_num = 0
	first_line = 1
	header_str = []
	file_name_base = output_dir + "DeathRecords_pt"
	current_output_file = file_name_base + str(file_num) + ".csv"

	os.mknod(current_output_file)
	f = open(input_file)
	csv_f = csv.reader(f)
	print(current_output_file)
	for line in csv_f:
		statinfo = os.stat(current_output_file)
		if (first_line):
			header_str = line
			first_line = 0
		elif (statinfo.st_size > MAX_FILE_SIZE_LIMIT_WITH_ROOM):
				file_num += 1
				current_output_file = file_name_base + str(file_num) + ".csv"
				statinfo = os.stat(input_file)
				add_line_to_file(header_str, current_output_file)
				print(current_output_file)
		add_line_to_file(line, current_output_file)

	return


break_large_file("../data_raw/_DeathRecords_ver14.csv", "../partitioned_files/")

#arr = return_file_as_array("../data_raw/SunSpotData.csv", 1)
#for line in arr:
#	add_line_to_file(line, "../data_raw/temp.csv")

#add_data_binary("../data_raw/_DeathRecords_ver8.csv", "../data_raw/MassShootings.csv", 1, "MassShootingOccurred","../data_raw/_DeathRecords_ver9.csv")

#add_daily_data("../data_raw/_DeathRecords_ver13.csv", "../data_raw/BasicDate.csv", 0, "1/1/2016", "Formatted Date", "../data_raw/_DeathRecords_ver14.csv")

# Used to add in federal holiday data
#add_data_binary("../data_raw/_DeathRecords_ver6.csv", "../data_raw/FullMoon.csv", 1, "IsFullMoon","../data_raw/_temp.csv")

# Used to estimate the mm/dd from the month and day of week
#estimate_dates_from_day_of_week_uniform("../data_raw/_DeathRecords_ver2.csv", 6, "../data_raw/temp.csv")

# Used to remove redundant columns of data, can be used again if more found redundant
#remove_list = ['Formatted Date']
#remove_column("../data_raw/_DeathRecords_ver12.csv", remove_list, "../data_raw/_DeathRecords_ver13.csv")