import codecs
import xml.etree.ElementTree as etree
import csv

f = etree.parse("BLex_03.xml")
lex = f.getroot()
search = lex.findall(".//p/italic")

# Daten aus CSV in dictionary einlesen
# NB: auf serv21 wird der CSV-Delimiter (;) aus irgendeinem Grund in einen Tabulator umgewandelt

with codecs.open("BurgenURL_2.csv", encoding="utf-8", errors="ignore") as infile:
    csv_r = csv.reader(infile, delimiter=";")
    next(csv_r)
    urls = list(csv_r)
    urls = {i[0]: i[1] for i in urls}

# XML-Datei mit dictionary keys abgleichen und links setzen

matches = 0

for entry in search:
    match = entry.text
    if match in urls.keys():
#        print("Writing url for: {}".format(match))
        matches += 1
        ext = etree.SubElement(entry, "ext-link")
        ext.text = match
        ext.set("xlink:href", urls[match])
        ext.set("ext-link-type", "uri")
        entry.text = None
        urls.pop(match, None)

print("NO CHANGES WRITTEN FOR: ")
for i in urls.keys():
    print(i)

#for i in urls:
 #   print(urls.get(i))
#print(len(urls))


# Ausgabedatei schreiben

f.write("outfile.xml")
#print("{} changes written.".format(matches))
