#!/bin/python3
import sys
if (len(sys.argv)-1) < 1 :
    print("none")
else:
    sys.argv.pop(0)
    parameters = sys.argv
    print("parameters: ",len(parameters))
    for i in range(len(parameters)) :
        print(parameters[i]," : ",len(parameters[i]))