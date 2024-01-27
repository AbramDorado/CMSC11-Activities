#TODO
from sys import argv, exit
import csv
from cs50 import SQL

#if argument is 2
if len(argv) == 2 and argv[1].endswith(".csv"):
    db = SQL("sqlite:///students.db") #put in database

    file = open(argv[1], 'r') #reads the file
    reader = csv.DictReader(file) #puts in dictionary

    for row in reader:
        names = row["name"]
        all_name = names.split()

        if len(all_name) == 2:
            f_name = all_name[0]
            l_name = all_name[1]
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?,?,?,?,?)", f_name, None, l_name, row["house"], row["birth"])

        elif len(all_name) == 3:
            f_name = all_name[0]
            m_name = all_name[1]
            l_name = all_name[2]
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?,?,?,?,?)", f_name, m_name, l_name, row["house"], row["birth"])

#error if no argument
else:
    print("Error, missing command-line argument(.csv file)!")
    exit(1)