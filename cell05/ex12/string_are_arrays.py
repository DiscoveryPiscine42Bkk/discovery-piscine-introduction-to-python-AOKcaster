#!/bin/python3
import sys
import re
if (len(sys.argv)-1) == 1 :
    z = re.findall("z",sys.argv[1])
    if not z:
        print("none")
    else :
        for i in range(len(z)):
            print("z", end='')
else:
    print("none")
