#TODO
from sys import argv, exit
import csv
from cs50 import SQL

#if argument is 2
if len(argv) == 2:
    db = SQL("sqlite:///students.db") #put in database
    all_rows = db.execute("SELECT DISTINCT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1])
    for row in all_rows:
        if row["middle"] != None:
            middle = row["middle"].strip()
            print(row["first"] + " " + middle + " " + row["last"] + ", born " + str(row["birth"]))
        else:
            print(row["first"] + " " + row["last"] + ",born " + str(row["birth"]))

#error if no argument
else:
    print("Error, missing command-line argument")
    exit(1)