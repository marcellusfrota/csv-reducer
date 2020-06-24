# -*- coding: utf-8 -*-
import pandas as pd
import os
import time
import argparse 

from pick import pick

'''
starting time
'''
start_time = time.time()

def main():

	clear()

	title_perm = 'CSV Reducer 0.1'

	parser = argparse.ArgumentParser(description=title_perm, epilog='let\'s reduce!')

	parser.add_argument('-i', '--input-file', type=str, dest='input_file', 
		help='CSV input file name', required=True)

	parser.add_argument('-o', '--output-file', type=str, dest='output_file', 
		help='CSV output file name', required=True)

	parser.add_argument('-d', '--remove-duplicate', type=str, default=False, 
		dest='remove_duplicate', help='Col or cols to check duplicate rows')

	parser.add_argument('-s', '--csv-separator', type=str, default=',', 
		dest='csv_separator', help='Caracter used to separate columns in CSV input/output file')

	parser.add_argument('-e', '--csv-encoding', type=str, default='iso-8859-1', 
		dest='csv_encoding', help='CSV encoding type, default is iso-8859-1')

	args = parser.parse_args()

	selected_cols = None

	try:

		df_header = pd.read_csv(args.input_file, encoding=args.csv_encoding, nrows=1, sep=args.csv_separator) # , usecols=['Nome', 'E-mail', 'CPF', 'Segmetacao']
 
		title = title_perm + '\n\nChoose columns to be used (press SPACE to mark, ENTER to continue): '
		options = df_header.columns.__dict__['_data']
		selected = pick(options, title, multiselect=True, min_selection_count=1)
		selected_cols = [x[0] for x in selected]

	except FileNotFoundError:
		print(":ERROR - CSV Input file do not exist.")

	if (args.remove_duplicate):
		duplicate_title = 'Choose columns to be checked for duplicates (press SPACE to mark, ENTER to continue): '
		duplicate_selected = pick(selected_cols, duplicate_title, multiselect=True, min_selection_count=1)
		duplicate_selected_cols = [d[0] for d in duplicate_selected]

	print(title_perm + "\n")

	try:
		df = pd.read_csv(args.input_file, encoding=args.csv_encoding, sep=args.csv_separator, usecols=selected_cols)
	except ValueError as error:
		print(":ERROR", error)

	if (args.remove_duplicate):
		df.drop_duplicates(subset=duplicate_selected_cols, keep='first', inplace=True)
		print(":Duplicates removed!")

	df.to_csv(args.output_file, encoding=args.csv_encoding, index=False, sep=args.csv_separator)

	print(":Done! have fun :)\n")
	print("--- end of execution in %s seconds ---" % (time.time() - start_time))

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux
    else: 
        _ = os.system('clear') 

if __name__ == "__main__":
	main()