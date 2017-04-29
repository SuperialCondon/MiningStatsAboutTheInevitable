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


def add_line_to_file(init_str,output_file_name):

	with open(output_file_name, "a") as f:
		f.write(init_str)
	return


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
		print("Reading in file "+filename)
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
def bayes_main(directory_path, data_list, output_file_name):
	C_index = 0
	complete_list = read_in_files_in_directory(directory_path, data_list)
	total = 0
	C_possibility_list = data_list[0][2]
	record_dict = {}
	X = ""

	# Establish dictionary to record 
	# loop through entire data list
	for i in range(1, len(data_list)):
		# loop through the outcome list
		X += data_list[i][0]
		X += " = "
		for result in data_list[i][2]:
			X += result
			X += ", "
			# investigated outcome list
			for item in C_possibility_list:
				record_dict[data_list[i][0]+result+data_list[0][0]+item[0]] = 0

	X = X[:-2]

	for item in complete_list:
		for possibility in C_possibility_list:
			if (item[C_index] == possibility[0]):
				possibility[1] += 1
		for i in range(1, len(item)):
			temp_str = data_list[i][0]+item[i]+data_list[0][0]+item[0]

			if temp_str in record_dict:
				record_dict[temp_str] += 1

		total += 1

	for total_item in C_possibility_list:
		line = ""
		this_item = total_item[0]
		check_for = data_list[0][0] + this_item
		mult = 1
		for item in record_dict:
			adder = 0
			if check_for in item:
				if (total_item[1] != 0):
					adder += (record_dict[item]/total_item[1])
					mult *= (record_dict[item]/total_item[1])
		mult *= (total_item[1]/total)
		line = line+"Probability "+data_list[0][0]+" = "+total_item[0]+" given " + X +", "+str(mult)+", "+str(total) +"\n"
		print(mult)
		#add_line_to_file(line,output_file_name)


# Data list in format -> [ [header_name, raw_index, [possibility_list] ], ...]
#data_list = [ ["buys_computer", 5, [["yes",0], ["no",0]]], 
#				["age", 1, ["<=30"]], 
#				["income", 2, ["medium"]], 
#				["student", 3, ["yes"]], 
#				["credit_rating", 4, ["fair"]] ]

#bayes_main("../from_slides/", data_list)

# data_list_full must be formatted like a list of the data_list objects.
#   [                  First objects                  ], [Secondary Objects]
# [ ["IsFederalHoliday", 37, [["True",0], ["False",0]]], ["Sex", 7, ["F"]] ]

def looper(directory_path, data_list_full, output_file_name):
	for sub_list in data_list_full:
		bayes_main(directory_path, sub_list, output_file_name)



data_list_full = [[ ["MannerOfDeath", 19, [["1",0], ["2",0], ["3",0], ["4",0], ["5",0], ["6",0], ["7",0], ["0",0]]], ["IsFullMoon", 39, ["True"]]],
					[ ["MannerOfDeath", 19, [["1",0], ["2",0], ["3",0], ["4",0], ["5",0], ["6",0], ["7",0], ["0",0]]], ["IsFullMoon", 39, ["False"]]] ]

#data_list_full = [ [ ["MannerOfDeath", 19, [["1",0], ["2",0], ["3",0], ["4",0], ["5",0], ["6",0], ["7",0], ["0",0]]], ["IsFullMoon", 39, ["True"]] ], 
#					[ ["MannerOfDeath", 19, [["1",0], ["2",0], ["3",0], ["4",0], ["5",0], ["6",0], ["7",0], ["0",0]]], ["IsFullMoon", 39, ["False"]] ] ]

directory_path = "../partitioned_files/"
output_file_name = "../results/MannerOfDeath_given_IsFullMoon.csv"

looper(directory_path, data_list_full, output_file_name)