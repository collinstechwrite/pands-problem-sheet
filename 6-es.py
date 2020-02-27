import sys
import os
"""This is a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.
e.g. $ python es.py moby-dick.txt
116960
"""

#Source1 https://stackabuse.com/command-line-arguments-in-python/"
#Source2 https://stackoverflow.com/questions/23232248/python-3-4-counting-occurrences-in-a-txt-file"

def main():
    """pass file name from command prompt get current working directory and file name in current working directory and count e"""
    current_directory = os.getcwd()
    current_file = current_directory + "\\" + str(sys.argv[1]) #sys.argv[1] is used to pass the file name from command prompt
    print("\nNow analysing " + current_file + "\nand counting the number of e(s)")

    file  = open(current_file, 'r').read() #open and read file
    analyse  = "e"
    count = file.count(analyse)
    print("\nNumber of e found: ", count)

main()
