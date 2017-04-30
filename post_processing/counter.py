#
# Author: Derek Gorthy
# Date: 4/20/2017
# Description: Used for counting occurances of events, typically with respect to date
#
# Notes: Run with Python3 
#

import csv
import os
import random
import collections


def add_line_to_file(init_str,output_file_name):

	with open(output_file_name, "a") as f:
		f.write(init_str)
	return


def dict_to_file(output_file, this_dict):

	od = collections.OrderedDict(sorted(this_dict.items()))

	for key in od:
		init_str = ""
		init_str = init_str + key
		for elem in this_dict[key]:
			init_str = init_str + "," + str(elem)
		init_str += "\n"
		add_line_to_file(init_str, output_file)

	return


def count_variations(input_directory_path, output_file_path, key_index, value_index, first_line, header_string, relevant_possibilities):

	temp_dict = {}

	for filename in os.listdir(input_directory_path):
		print("Reading in file "+filename)
		f = open(input_directory_path+filename)
		csv_f = csv.reader(f)
		first_line = True

		for row in csv_f:
			if(first_line):
				first_line = False
			else:
				if row[key_index] not in temp_dict:
					this_value = []
					for i in range(0,len(relevant_possibilities)):
						this_value.append(0)
					temp_dict[row[key_index]] = this_value
				for i in range(0,len(relevant_possibilities)):
					if (relevant_possibilities[i] == row[value_index]):
						temp_dict[row[key_index]][i] += 1

	header_string += "\n"
	add_line_to_file(header_string, output_file_path)
	dict_to_file(output_file_path, temp_dict)
				
	return

count_variations("../partitioned_files/", "../totals/total_deaths_by_AgeRecord12.csv", 13, 19, 1, \
	"AgeRecode12, Not Specified, Accident, Suicide, Homicide, Pending Investigation, Could Not be Determined, Self-inflicted Natural", \
	 ["0","1","2","3","4","5","6","7"])
