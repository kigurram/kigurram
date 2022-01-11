# Write some string to file
#file_object = open("D:\kiran_python\\txt.txt", "w")
#st = input("Enter Some string")
#file_object.write(st)
#file_object.close()

# Append some string to file
#file_object = open("D:\kiran_python\\txt.txt", "a")
#st = input("Enter Some string")
#file_object.write("\n"+st)
#file_object.close()

# Read a file
#file_object = open("D:\kiran_python\\txt.txt", "r")
#st = file_object.read()
#print(st)
#file_object.close()

# Read and split lines file
#file_object = open("D:\kiran_python\\txt.txt", "r")
#st = file_object.read().splitlines()
#print(st)
#file_object.close()

# Check file exists and Append some string to file
'''
import os

if os.path.isfile("D:\kiran_python\\txt.txt"):
    file_object = open("D:\kiran_python\\txt.txt", "a")
    st = input("Enter Some string")
    file_object.write("\n"+st)
    file_object.close()
else:
    print('File not found')
'''

# Read file with WITH statement
'''
with open("D:\kiran_python\\txt.txt", "r") as f:
    for line in f:
        print(line)
'''