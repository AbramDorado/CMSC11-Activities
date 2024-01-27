from sys import argv, exit
import csv

#Function to get the values
def get(n, sub):
    ret = [0] * len(n)
    for i in range(len(n) - len(sub), -1, -1):
        if n[i: i + len(sub)] == sub:
            if i + len(sub) > len(n) - 1:
                ret[i] = 1
            else:
                ret[i] = 1 + ret[i + len(sub)]
    return max(ret) #return the value

#Function to see if there is a match
def check(reader, data):
    for line in reader:
        person = line[0]
        values = [ int(val) for val in line[1:] ]
        if values == data:
            print(person)
            return
    print("No match") #if there is no match in dna

#Main function to execute the program
def main():
    #if the command line is not complete
    if len(argv) != 3:
        print("missing command-line argument")
        exit(1)

    with open(argv[1], "r") as name_data:
        reader = csv.reader(name_data)
        sequences = next(reader)[1:]

        with open(argv[2]) as  file:
            n = file.read()
            data = [get(n, seq) for seq in sequences]

        check(reader, data)

#Run
if __name__ == "__main__":
    main()