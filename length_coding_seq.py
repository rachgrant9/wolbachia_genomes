# length_of_coding_seq.py sequence.txt

import sys

coding = open(sys.argv[1])
counter = 0
for line in coding:
    if not line.startswith('>'):
       counter = counter + len(line)
print(counter)
