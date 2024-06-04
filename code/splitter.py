#
#
#
#

import sys


def read_file(filename):
    """ opens and reads file with name filename and returns a string of text """
    infile = open(filename, "r")
    text = infile.read()
    infile.close()
    return text

def main():
    if len(sys.argv) != 4:
        print("3 arguments are expected: a file, amount of lines and output file.")
        exit(-1)
    if sys.argv[1][-4:] != ".tok":
        print("You have to input a .tok file to split.")
        exit(-1)
    if sys.argv[2].isnumeric() == False:
        print("You have to enter an amount of lines")
        exit(-1)

    file1 = read_file(sys.argv[1])
    amount = int(sys.argv[2])
    filename = sys.argv[3]
    lines = file1.split("\n")
    
    with open(filename + ".tok", "w") as file:
        file.writelines(line + '\n' for line in lines[:amount])


if __name__ =="__main__":
    main()