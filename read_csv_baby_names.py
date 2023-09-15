import csv
YEAR = "1980"
SEX = "boy"

with open('DATA/baby-names.csv') as baby_names_in:
    rdr = csv.reader(baby_names_in)
    next(rdr)  # consume next line
    for year, name, pct, sex in rdr:
        if (year == YEAR) and (sex == SEX):
            print(name)