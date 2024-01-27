# 1. define a function for reading files and return the contents of the file as list of 'floats'.
def read_file():
    file_name = input("Enter filename (including the file type) to read: ")
    list_grades = []
    # implement file reading here

    #To check if the file exist or not 
    try: 
        f = open(file_name)
        for line in f.readlines():
            list_grades.append(float(line))
            f.close()
        return list_grades
    except FileNotFoundError: #if no file, return false
        return False

import statistics
# 2. define a function that calculates the mean of the grades stored in a list.
def mean(list_grades):
    display_barchart(list_grades)
    # implement mean

    sum_num = 0
    for t in list_grades:
        sum_num = sum_num + t  #add the grades         

    mean = sum_num / len(list_grades) #divide to the nummber of grades
    print("\nThe mean grade of students is %.2f" %mean) 

# 4. define a function that calculates the median of the grades stored in a list.
def median(list_grades):
    display_barchart(list_grades)
    # implement median

    n = len(list_grades)
    list_grades.sort()
    
    if n % 2 == 0: #if list is even
        median1 = list_grades[n//2]
        median2 = list_grades[n//2 - 1]
        median = (median1 + median2)/2 #combinde the two median and get the average
    else:
        median = list_grades[n//2] #if list is odd
    print("\nThe median grade of students is %.2f" % median)

from collections import Counter
# 5. define a function that calculates the mode of the grades stored in a list.
def mode(list_grades):
    # assume that the distribution is unimodal
    display_barchart(list_grades)
    # implement mode

    length = len(list_grades) 
    data = Counter(list_grades) #counting multiple elements
    access = dict(data)         #storing in dictionary
 
    # filter the a values with the highest b values
    #a is the values in sorted list_grades
    #b is the occurrences of each value in list_grades
    new_list = [a for a, b in access.items() if b == max(list(data.values()))]
    mode = new_list[0]   #accessing list

    #conditions if there is a mode in the list
    if len(new_list) == length: #if length is equals to new  created list
        print("No mode found")
    else:
        print("\nThe mode grade of students is %.2f" % mode)

#auxiliary function  
def print_loop(occurrences):
    print("1.00 ", end="") #print the labled grade

    for i in range (0,occurrences): #for loop to loop the "@" symbol
        print("@", end="")

    print(" (%i)"%occurrences) #print the number of occurrences

# 6. implement a function that prints out a bar chart
def display_barchart(list_grades):
    print("\nDistribution of Grades")
    print("----------------------")

    #count the number of each element in the list (the grades)
    #And print it using the auxiliary function
    a = list_grades.count(1.00)
    print_loop(a)
    b = list_grades.count(1.25)
    print_loop(b)
    c = list_grades.count(1.50)
    print_loop(c)
    d = list_grades.count(1.75)
    print_loop(d)
    e = list_grades.count(2.00)
    print_loop(e)
    f = list_grades.count(2.25)
    print_loop(f)
    g = list_grades.count(2.50)
    print_loop(g)
    h = list_grades.count(2.75)
    print_loop(h)
    i = list_grades.count(3.00)
    print_loop(i)
    j = list_grades.count(4.00)
    print_loop(j)
    k = list_grades.count(5.00)
    print_loop(k)

    students = len(list_grades) #calculate the number of students that wa s transfered to the list
    print("\nNumber of students: ", students)
    
# 7. using conditions, complete the display_menu()
def display_menu():
    print("""----------------------------------------------------
    Main Menu:
    [1] Find the mean of grades.
    [2] Find the median of grades.
    [3] Find the mode of grades.
    [4] Find the mean, median, and mode of grades.
    [5] Exit program.
    """)
    choice = input("Enter choice: ")

    #conditions according to the input
    if choice == '1':
        mean(grades)
    elif choice == '2':
        median(grades)
    elif choice == '3':
        mode(grades)
    elif choice == '4':
        mean(grades)
        median(grades)
        mode(grades)
    elif choice == '5':
        exit()
    return choice

if __name__ == "__main__":
    print("\nMeasures of Central Tendency\n")
    # open file
    grades = read_file()

    if grades != False: #condition if file is in the directory
        choice = display_menu()
        
        while choice != '5': #loop the main menu if not '5'
            display_menu()
    else:
        print("No such file found") #no file


"""SAMPLE OUTPUT
Distribution of Grades
----------------------
1.00 @@@@@@@@@@@@@@@@@@@@@@@@ (24)
1.25 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (40)
1.50 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (69)
1.75 @ (1)
2.00 @@@@@@@@@@@@@@@@@ (17)
2.25 @@@@@@@@@@@@@@@@@@@@@@@@@@@@ (28)
2.50 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (46)
2.75 @@@@@@@@@@@@@@@@@@@ (19)
3.00 @@@@@@@@@@@ (11)
4.00 @@@@@@@ (7)
5.00 @@@@@ (5)

Number of students: 267 

The mean grade of students is %{.2}f.
"""