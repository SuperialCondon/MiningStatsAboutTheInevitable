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


# Assuming that each partial dataset has a header
#
# directory_path -> directory that holds partial dataset
# data_list -> single Bayesian calculation
#
def read_in_files_in_directory(directory_path, data_list):
	complete_list = []
	indice_list = []

	for item in data_list:
		indice_list.append(item[1])

	# Iterate through every file in directory
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
				# Store only needed elements, not every element
				for i in range(0, len(indice_list)):
					this_line.append(row[indice_list[i]].strip())
				file_list.append(this_line)

		complete_list += file_list

	return (complete_list)


# directory_path -> directory that holds partial dataset
# data_list -> single Bayesian calculation
# output_file_name -> Bayesian output file with file path 
#
def bayes_main(directory_path, data_list, output_file_name):
	C_index = 0
	complete_list = read_in_files_in_directory(directory_path, data_list)
	total = 0
	C_possibility_list = data_list[0][2]
	# Due to the size of the set, dictionary is efficient enough to store each possibility
	record_dict = {}
	X = ""

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

	# For every stored element, place into dictionary
	for item in complete_list:
		for possibility in C_possibility_list:
			if (item[C_index] == possibility[0]):
				possibility[1] += 1
		for i in range(1, len(item)):
			temp_str = data_list[i][0]+item[i]+data_list[0][0]+item[0]

			if temp_str in record_dict:
				record_dict[temp_str] += 1

		total += 1

	# Now, loop through the stored dictionary and perform Bayesian calculation
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
		add_line_to_file(line,output_file_name)


# Simple looping function if multiple Bayesian calculations need to be run
#
def looper(directory_path, data_list_full, output_file_name):
	for sub_list in data_list_full:
		bayes_main(directory_path, sub_list, output_file_name)


# EXAMPLE USAGE:
#
#data_list_full = [[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["1"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["2"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["3"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["4"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["5"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["6"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["7"]]],
#					[ ["ResidentStatus", 2, [["1",0], ["2",0], ["3",0], ["4",0]]], ["MannerOfDeath", 19, ["0"]]]
#					]

#directory_path = "../partitioned_files/"
#output_file_name = "../results/MannerOfDeath_given_ResidentStatus.csv"
#looper(directory_path, data_list_full, output_file_name)