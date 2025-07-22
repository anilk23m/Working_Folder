f = open("file1.txt", "a")
f.write("this is the last line to the file")

#r+ does read and write but here pointer is at the beginning - no truncate
#w+ does the truncate of the file and overwrite the file - truncate
#a+ does the read and append at the end of the file and pointer is at the end- no truncate

