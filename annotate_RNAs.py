import sys
import re

files=sys.argv[1:] #captures a list of input files from the command line


with open("ncRNA.txt", 'w') as out:

        for file in files:
                name=file.split('/')[-1]
                out.write(name + '\n')

                with open(file, 'r') as f:
                        for line in f:
                                if re.search("RNA", line):
                                        out.write(line)
