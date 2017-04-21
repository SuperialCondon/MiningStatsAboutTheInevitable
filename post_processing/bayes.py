#
# Author: Derek Gorthy
# Date: 4/20/2017
# Description: Script for Bayesian probabilities. 
#
# Notes: Run with Python3 
#

import csv
import os
import random


def get_indice_list(directory_path, needed_rows):
	indice_list = []
	print(needed_rows)
	for filename in os.listdir(directory_path):
		f = open(directory_path+filename)
		csv_f = csv.reader(f)

		for row in csv_f:
			for i in range(0, len(row)):
				if (row[i].strip() in needed_rows):
					indice_list.append(i)
					print(i)

			return indice_list


def read_in_files_in_directory(directory_path, needed_rows):
	complete_list = []
	indice_list = get_indice_list(directory_path, needed_rows)

	for filename in os.listdir(directory_path):
		f = open(directory_path+filename)
		csv_f = csv.reader(f)
		first_line = True
		file_list = []

		for row in csv_f:
			this_line = []

			if (first_line):
				first_line = False
				
			else:
				for i in range(0, len(indice_list)):
					this_line.append(row[indice_list[i]].strip())
				file_list.append(this_line)

		complete_list += file_list

	print(complete_list)


needed_rows = ["age", "income"]
read_in_files_in_directory("../from_slides/", needed_rows)


# H_list -> [(H_1, H_2, ...)] -> what we are looking for given A
# A_list -> [(X_1, X_2, ...)] -> the known conditional 
#def find_prob_H_given_X(H_list, X_list):



# ignore values in format = [(Column_Header, Data_value_str),(...]
#ignore_values = [()]