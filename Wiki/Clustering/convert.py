import csv

with open("stripped-agg-all-days") as fin, open("ur_outfile", 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())