# Shubhayu Shrestha 1001724804
# CSE 3302-003 Kelly French
# Compiled with 'perl 5, version 30, subversion 2 (v5.30.2) 
# built for darwin-thread-multi-2level' on MacOS

# use statements
use strict;
use warnings;
use Cwd;

# function that will return size of the directory
sub DirectorySize
{
    # initializing a local variable that will hodl the total size of the current directory 
    # it is searching
    my $localTotalSize = 0;

    # storing the current directory that we pass in into a variable called currentDir
    my ($currentDir) = @_; 

    # glob() function prints the files present in a directory 
    # initializing array 
    my @files = glob($currentDir);

    # iterating through the files
    foreach(@files)
    {
        # checking if the current file is a file
        if (-f $_) 
        {
            # incrementing total size by the size of the file
            $localTotalSize += -s $_; 
        }
        # checking if the current file is a directory
        if (-d $_) 
        {
            # recurisively calling the directory size
            $localTotalSize += DirectorySize("$_/*"); 
        }
    }
    return $localTotalSize;
}

# "main"

# holding the current working directory in variable called cwd
my $cwd = getcwd();

$cwd="$cwd/*";

# storing the total size of the direcotry in a variable called totalSize which will keep 
# calling directory size recusively until no more files are left
my $totalSize = DirectorySize($cwd); 

# printing out the total size of the directory
print("TOTAL SIZE: $totalSize bytes\n"); 
