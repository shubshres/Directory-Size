// Shubhayu Shrestha 1001724804
// CSE 3302-003 Kelly French
// Compiled with Java 'openjdk 16.0.1 2021-4-20' on MacOS

// Import statements
import java.io.File;
import java.lang.ref.Cleaner;

public class sxs4805_lab01 
{
    public static void main(String[] args)
    {
        // getting the current directory
        String currentDirectory = System.getProperty("user.dir");

        // creating a long variable that will hold the size of the directory
        // path traversing through the directory an d
        long totalSize = DirectorySize(currentDirectory); 

        // Printing out total size in bytes
        System.out.println("\nTOTAL SIZE: " + totalSize + " bytes\n"); 
    }

    public static long DirectorySize(String currentDirectory)
    {
        // initializing a local variable that will hold the total size of the 
        // current directory it is searching
        long totalSize = 0; 

        // storing the path of the working directory 
        File currWorkDir = new File(currentDirectory); 

        // creating an array that holds the files and subdirectories from the current
        // directory in an array
        String[] files = currWorkDir.list(); 

        // creating a ranged based for loop that will traverse through the array
        for(int i = 0; i < files.length; i++)
        {
            // Creating a variable that holds the next path 
            File tempFile = new File(currentDirectory + "/" + files[i]); 
            
            // if the next file is a directory, then we will recusively call this function
            if(tempFile.isDirectory())
            {
                // if directory is found, we will recursively call directory size
                totalSize+=DirectorySize(currentDirectory + "/" + files[i]);
            }
            // if the next file is a file, then we will check the size and add it to the total size
            else if(tempFile.isFile())
            {
                // adding file size to total size
                totalSize+=tempFile.length(); 
            }
        }
        return totalSize; 
    }
}
