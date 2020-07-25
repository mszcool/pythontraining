#
# Working with files
#

def main():

    # Open a file for writing and create it if it does not exists
    # f = open("textfile.txt", "w+")  # w = write, + = create if not exists

    # Open a file for appending text at the end
    #f = open("textfile.txt", "a")     # a = append

    # Write lines of data to a file
    # for i in range(10):
    #     f.write("Line Number " + str(i) + "\r\n")

    # Close the file
    # f.close()

    # Open file to read contents
    f = open("textfile.txt", "r")      # r = read
    if f.mode == 'r':
        # contents = f.read()   # Reads everything
        # print(contents)

        # fl = f.readlines()
        # for l in fl:
        #     print(l)

        fl = f.readline(20)     # Parameter is the max number of characters to read from the line
        while(fl != ""):
            print(fl)
            fl = f.readline(20)


if __name__ == "__main__":
    main()