import csv

with open("en-pagecounts-20081011-000000") as fin, open("ur_outfile", 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())