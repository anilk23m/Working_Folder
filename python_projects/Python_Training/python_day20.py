# #with statement - context manager
#it automatically close the file even if an error occurs. No need to remember file.close()

with open("file1.txt", "r") as file:
    line = file.read()
    print(line)

with open("file1.txt", "w") as file:
    file.write("This is first line\n")
    file.write("This is second line\n")
    file.write("This is third line\n")
    file.write("This is fourth line\n")
    file.write("This is fifth line\n")
    file.write("This is sixth line")

lines = ["test_login: PASS\n",
         "test_search: FAIL\n",
         "test_checkout: PASS\n",
         "test_payment: FAIL"
         ]
with open("file1.txt", "w") as file:
    file.writelines(lines)

with open("file1.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"line1: {line1}")
    print(f"line2: {line2}")

res  = []
with open("file1.txt", "r") as file:
    for line in file:
        print(line.strip().strip("&"))

#append = a - adds to end of line, doesn't overwrite
with open("file1.txt", "a") as file:
    file.write("\nthis is the append line")
    file.write("\nthis is another append line")


import os
filename = "file1.txt"
if os.path.exists(filename):
    print("file exists")
else:
    print("file does not exist")
#r+ - read&write - no file create - and no overwrite
#w+ - write & read - file creates if no file - overwrite also
#a+ - append & read - file create and no ovewrite

