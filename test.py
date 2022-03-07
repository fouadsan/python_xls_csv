import csv

file = open('csvExample.csv')

csvreader = csv.reader(file)

print(csvreader)

rows = []
for row in csvreader:
    print(row)
    for value in row:
        print(type(value))
        # rows.append(row)
# print(rows)
# 601,OUAZAA LYAZID,,783151950,,1,,,,,,,,,,,,,