import codecs
import argparse
import xml.etree.ElementTree as etree
import csv

#f = etree.parse(xfile)
#lex = f.getroot()
#search = lex.findall(target)

class xml_enhancer():
    
    def __init__(self, xfile):
        self.xfile = open(xfile, "rb")
        self.element_tree = etree.parse(xfile)
        return xfile

    def parse_data(self, filename):
        with codecs.open(filename, encoding="utf-8", errors="ignore") as infile:
            csv_r = csv.reader(infile, delimiter=";")
            next(csv_r)
            data = list(csv_r)
            data = {i[0]: i[1] for i in data}
            return data
    
    def set_target(self, xpath):
        search = xile.findall(xpath)
        return search

    def set_element():
        pass        

item = xml_enhancer("BLex_03.xml")
item.parse_data("BurgenURL_2.csv")
print(item.set_target(".//p/italic"))


# Daten aus CSV in dictionary einlesen
# NB: auf serv21 wird der CSV-Delimiter (;) aus irgendeinem Grund in einen Tabulator umgewandelt




"""
matches = 0

for entry in search:
    match = entry.text
    if match in urls.keys():
        print("Writing url for: {}".format(match))
        matches += 1
        ext = etree.SubElement(entry, "ext-link")
        ext.set("xlink:href", urls[match])
        ext.set("ext-link-type", "uri")

# Ausgabedatei schreiben

f.write("outfile.xml")
print("{} changes written.".format(matches))

"""
