#
#
#
#

import sys
from splitter import read_file

def main():
    if len(sys.argv) != 4:
        print("3 arguments are expected: a gold standard .conll file, a shorter .conll file and a file to write to.")
        exit(-1)
    if sys.argv[1][-6:] != ".conll" and sys.argv[2][-6:] != ".conll":
        print("You have to input a .conll file to split.")
        exit(-1)

    file1 = read_file(sys.argv[1])
    file2 = read_file(sys.argv[2])
    filename = sys.argv[3]
    lines1 = file1.split("\n")
    lines2 = file2.split("\n")

    print(len(lines2))
    print(len(lines1[:len(lines2)]))

    with open(filename + ".conll", "w") as file:
        file.writelines(line + '\n' for line in lines1[:len(lines2) - 2])
        file.write("#end document")

if __name__ == "__main__":
    main()
