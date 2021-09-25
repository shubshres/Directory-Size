# Shubhayu Shrestha 1001724804
# CSE 3302-003 Kelly French
# Compiled with Python 3.9.5 on MacOS

# Import Statements
import os

# recursive function that will search through the directory path through all of the folders until
# a file is seen and will add that file size to the total size
def directory_search(current_directory):
    # Storing the files and sub-directories from current directory in an array
    files = os.listdir(current_directory)
    
    # initializing variable that will hold the total file size
    total_size = 0

    # looping through the files in the current working directory and checking if it is either
    # a file or a directory, if it is a directory, it will recursively call the function
    # if it is a file, it will check the file size and add it to the total size
    for x in files:
        # creating variable that holds the next path
        nextpath = os.path.join(current_directory, x)

        # if the next file is a directory, then we will recursively call this function 
        if os.path.isdir(nextpath):
            #if directory is found, change the directory 
            total_size += directory_search(nextpath)

        # if the next file is a file, then we will check the size and add it onto total size
        elif os.path.isfile(nextpath):
            # initializing file_size - a temp variable that will hold the current size of the file
            file_size = os.path.getsize(nextpath)
            # adding file size to total size
            total_size += file_size

    return total_size


# Checking the current initial working directory and storing the current working directory
# in a variable called path
# User or GTA can also change this file path to another file path on their computer
# path variable that holds the current working directory
current_directory = os.getcwd()

# print statement that will print the total number of bytes after searching
# through the current directory
print("TOTAL SIZE: %d bytes" % directory_search(current_directory))
