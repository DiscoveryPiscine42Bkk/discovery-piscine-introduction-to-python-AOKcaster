#!/bin/python3
import sys
if (len(sys.argv)-1) == 1 :
    x = input("What was the parameter? ")
    if x == sys.argv[1] :
        print("Good job!")
    else :
        print("Nope, sorry...")
else:
    print("none")