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



def generate_partitioned_set(input_directory_path, output_file_path, key_index, value_index, first_line, header_string, relevant_possibilities):

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
				print(row[key_index])
				if(row[key_index] not in temp_dict):
					this_value = []
					for i in range(0,len(relevant_possibilities)):
						this_value.append(0)
				for i in range(0,len(relevant_possibilities)):
					if (relevant_possibilities[i] == row[value_index]):
						temp_dict[row[key_index]][i] += 1
	for key in temp_dict:
		print(key, " ", temp_dict[key])		
				
	return

generate_partitioned_set("../partitioned_files/", "nil", 44, 19, 1, "Date, Accident, Suicide, Homicide, Natural", ["1","2","3","7"])