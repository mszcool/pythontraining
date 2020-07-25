#
# Explore OS interaction with Python
#

import os
from os import path
import datetime
import time

def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    fexists = path.exists("textfile.txt")
    isfile = path.isfile("textfile.txt")
    isdir = path.isdir("textfile.txt")
    print("Item exists: ", fexists)
    print("Is a file: ", isfile)
    print("Is a directory: ", isdir)

    # Work with file paths
    fullPath = path.realpath("textfile.txt")
    print(fullPath)
    print("Filename and path " + str(path.split(fullPath)))
    print("- path: ", path.split(fullPath)[0])
    print("- file: ", path.split(fullPath)[1])

    # Get the modification time
    modifiedAt = time.ctime(path.getmtime("textfile.txt"))
    createdAt = time.ctime(path.getctime("textfile.txt"))
    print("Created at ", createdAt, " and modified at ", modifiedAt)
    print("Modified at ", datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getctime("textfile.txt"))
    print("Has been modified ", td, " ago!")
    print("Has been modified ", td.total_seconds(), " seconds ago!")

if __name__ == "__main__":
    main()