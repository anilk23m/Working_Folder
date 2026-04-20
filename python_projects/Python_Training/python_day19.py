#file handling lets you read from file and write to file on your system - text file, csv file, json, log file etc.
#Automation scenario - This is essential in automation for reading test data, writing reports, parsing logs etc.

#open() - function
#open(filename, mode) - syntax
file_cont = open("file1.txt", "r")
lines = file_cont.read()
print(lines)
file_cont.close()

file = open("file1.txt", "w")
file.write("Hello World")
file.close()

