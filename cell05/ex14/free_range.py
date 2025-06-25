#!/bin/python3
import sys
new = []
num = 1
if (len(sys.argv)-1) == 2 :
    sys.argv.pop(0)
    new.append(int(sys.argv[0]))
    for i in range(int(sys.argv[0]),int(sys.argv[1])) :
        new.append(int(sys.argv[0])+num)
        num += 1
    print(new)
else:
    print("none")