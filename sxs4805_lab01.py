# Shubhayu Shrestha 1001724804
# CSE 3302-003 Kelly French
# Compiled with Python 3.9.5 on MacOS

# Import Statements
import os

def directory_search(current_directory):
    # DEBUG printing current directory
    print("\n\t"+current_directory)

    # Storing the files and sub-directories from current directory in an array
    files = os.listdir(current_directory)
    
    # DEBUG: printing contents of array
    print("\n\nPRINTING ARRAY \n")
    print(files)

    total_size = 0
    # looping through the files in the directory
    for x in files:
        # storing a variable that holds the next path 
        nextpath = os.path.join(current_directory, x)

        if os.path.isdir(nextpath):
            # DEBUG
            print("\n\nCHANGING DIRECTORY TO " + x)

            #if directory is found, change the directory
            total_size+=directory_search(nextpath)
            
        elif os.path.isfile(nextpath):
            file_size = 0
            file_size = os.path.getsize(nextpath)

            # DEBUG
            print(x + " is a file and is ", file_size, " bytes")

            # checking and adding the size of the file to the TotalSize
            total_size += file_size
    
    return total_size


# DEBUG
print("\n\n\n\n\nSTARTING HERE")

# Checking the current initial working directory and storing the current working directory
# in a variable called path
# User or GTA can also change this file path to another file path on their computer
# path variable that holds the current working directory
current_directory = os.getcwd()
print("\n\nTOTAL SIZE: %d BYTES..." %directory_search(current_directory))
        





