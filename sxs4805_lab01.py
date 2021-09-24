# Shubhayu Shrestha 1001724804
# CSE 3302-003 Kelly French

# Import Statements
import os

files = []

# Checking the current working directory and storing the current working directory in a variable called path
path = os.getcwd()

if os.path.isdir(path):
    print("is directory")
elif os.path.isfile(path):
    print("is file")