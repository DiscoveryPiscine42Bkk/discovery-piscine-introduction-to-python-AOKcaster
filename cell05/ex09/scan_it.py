#!/bin/python3
import sys
import re
if (len(sys.argv)-1) == 2 :
    answer = re.findall(sys.argv[1],sys.argv[2])
    print(len(answer))
else:
    print("none")

