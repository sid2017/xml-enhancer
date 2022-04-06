#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import csv

# Daten aus CSV in dictionary einlesen
# NB: auf serv21 wird der CSV-Delimiter (;) aus irgendeinem Grund in einen Tabulator umgewandelt

with open("BurgenURL_2.csv") as infile:
	csv_r = csv.reader(infile, delimiter="\t")
	next(csv_r)
	urls = list(csv_r)
	urls = {i[0]:i[1] for i in urls}
#	print(urls)

# Suchmuster generieren

patterns = []

for i in urls.keys():
	my_str = "<italic>" + i  + "</italic>"
	patterns.append(my_str)

# XML-Datei durchsuchen

f = open("blex_test.xml", "r")
matches = 0

for p in patterns:
	print(p)	



# XML-Modifikation mit re (testweise)

#f.write("output.xml")
#	match = re.search("\<italic>[a-zA-Z]*\<\/italic\>" ,entry.text)
#	print(match)
#	if match in burgen:
#		print(match)
#		matches += 1
	

#print("I found {} matches.".format(matches))



#print(pattern)
