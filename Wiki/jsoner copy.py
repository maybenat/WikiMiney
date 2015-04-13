import csv
import json

csvfile = open('ur_outfile.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Language","Page_Name","Views","Bytes")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')