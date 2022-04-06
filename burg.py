import csv
import os

def ReadCSVasDict(csv_file):
	try:
		with open(csv_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print row['id'], row['name'], row['region'], row['land']
	except IOError as err:
		print("I/O error({0})".format(err))
	return

currentPath = os.getcwd()
csv_file = currentPath + "/test.csv"

ReadCSVasDict(csv_file)
