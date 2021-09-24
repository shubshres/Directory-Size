/* 
Author: Shubhayu Shrestha 1001724804

Program Details: Write a program to calculate the total size of all files in the current directory / folder and all sub-folders. 
The code should be runnable on the Omega server (netid@omega.uta.edu) without any configuration.  

This program will be written in C. 
*/

// include guards
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h> // alows us to utilize directory traversing
#include <unistd.h>

// creating defines
#define MAX_COMMAND_SIZE 255 // creating a define that is the maximum command-line size
#define _POSIX_SOURCE

// Function that will return the sum size 
long int DirSize(long int *size)
{

}

int main()
{
    // 
    DIR *current_directory; 
    current_directory = opendir("."); // opening directory the user is currently in

    // error handling to see if the current directory is able to be opened or not
    if(current_directory == NULL)
    {
        perror("ERROR: NO DIRECTORY FOUND");
        return(1); // exit the program 
    }

    // initializing variable called size that will hold the current size of the files. 
    //long int size += DirSize(&size); 
    
    // Code finished without any errors
    return 0; 
}
