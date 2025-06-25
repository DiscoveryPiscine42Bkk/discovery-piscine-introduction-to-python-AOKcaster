#!/bin/python3
import sys
import re
new = []
if (len(sys.argv)-1) > 0 :
    sys.argv.pop(0)
    for i in range(len(sys.argv)):
        if re.findall("ism",sys.argv[i]):
            pass
        else :
            new.append(sys.argv[i]+"ism")
    for i in range(len(new)):
        print(new[i])
else:
    print("none")
