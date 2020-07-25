#
# Interacting with the OS shell
#

import os
from os import path
import shutil
from zipfile import ZipFile

def main():

    # make a duplicate of an existing file

    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        sourceFile = path.realpath("textfile.txt")

        # Make a backup copy by appending "bak" to the name
        destFile = sourceFile + ".bak"

        # copy over the permissions, modification times and other info
        shutil.copy(sourceFile, destFile)       # Copy the file
        shutil.copystat(sourceFile, destFile)   # Copy the attributes

        # rename the original file
        newFile = path.realpath("newtextfile.txt")
        if path.exists(newFile):
            os.remove(newFile)
        os.rename("textfile.txt.bak", "newtextfile.txt")

        # put things into a ZIP-file (Puts all content of rootDir into ZIP-archive)
        #rootDir, tail = path.split(sourceFile)
        #shutil.make_archive("archive", "zip", rootDir)

        with ZipFile("testzip.zip", "w") as newArchive:
            newArchive.write("textfile.txt")
            newArchive.write("newtextfile.txt")

if __name__ == "__main__":
    main()