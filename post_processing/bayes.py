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

# Redundant function, refactor to remove
def get_c_index(directory_path, c,):
	for filename in os.listdir(directory_path):
		f = open(directory_path+filename)
		csv_f = csv.reader(f)

		for row in csv_f:
			for i in range(0, len(row)):
				if (row[i].strip() == c):
					return i


def get_indice_list(directory_path, needed_rows):
	indice_list = []
	for filename in os.listdir(directory_path):
		f = open(directory_path+filename)
		csv_f = csv.reader(f)

		for row in csv_f:
			for i in range(0, len(row)):
				if (row[i].strip() in needed_rows):
					indice_list.append(i)
			return indice_list


def read_in_files_in_directory(directory_path, data_list):
	complete_list = []
	indice_list = []

	for item in data_list:
		indice_list.append(item[1])

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

	return (complete_list)


# C is the single value that we care about, X will be rest of list
def bayes_main(directory_path, data_list):
	C_index = 0
	complete_list = read_in_files_in_directory(directory_path, data_list)
	total = 0
	C_possibility_list = data_list[0][2]

	for item in complete_list:
		for possibility in C_possibility_list:
			if (item[C_index] == possibility[0]):

				possibility[1] += 1

		total += 1


# Data list in format -> [ [header_name, raw_index, [possibility_list] ], ...]
data_list = [ ["buys_computer", 5, [["yes",0], ["no",0]]], 
				["age", 1, ["yes", "no"]], 
				["income", 2, ["yes","no"]], 
				["student", 3, ["yes","no"]], 
				["credit_rating", 4, ["yes","no"]] ]

bayes_main("../from_slides/", data_list)


# H_list -> [(H_1, H_2, ...)] -> what we are looking for given A
# A_list -> [(X_1, X_2, ...)] -> the known conditional 
#def find_prob_H_given_X(H_list, X_list):



# ignore values in format = [(Column_Header, Data_value_str),(...]
#ignore_values = [()]