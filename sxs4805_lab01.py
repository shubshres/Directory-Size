# Shubhayu Shrestha 1001724804
# CSE 3302-003 Kelly French
# Compiled with Python 3.9.5 on MacOS

# Import Statements
import os

totalSize = 0

def directory_search():

    # Checking the current initial working directory and storing the current working directory
    # in a variable called path
    # User or GTA can also change this file path to another file path on their computer
    # path variable that holds the current working directory
    current_directory = os.getcwd()

    # DEBUG printing current directory
    print("\n\t"+current_directory)

    # Storing the files and sub-directories from current directory in an array
    files = os.listdir(current_directory)
    
    # DEBUG: printing contents of array
    print("\n\nPRINTING ARRAY \n")
    print(files)

    # going back a directory
    if files == []:
        # DEBUG
        print("EMPTY")
        os.chdir("..")
        

    # looping through the files in the directory
    for x in files:
        file_size = 0
        file_size = os.path.getsize(x)
       
        # DEBUG
        print(x + " is a file and is ", file_size, " bytes")

        
        # checking and adding the size of the file to the TotalSize
        global totalSize
        totalSize += file_size
        print("\t\tTotal Size is: %d Bytes" %totalSize)

        if os.path.isdir(x):
            # DEBUG
            print("\n\nCHANGING DIRECTORY TO " + x)

            #if directory is found, change the directory
            os.chdir(x)
            directory_search()


# DEBUG
print("\n\n\n\n\nSTARTING HERE")

directory_search()
print("\n\nTOTAL SIZE: %d BYTES..." %totalSize)
