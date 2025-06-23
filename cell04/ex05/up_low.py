#!/bin/python
import math
num = str(input())
for i in num :
    if i.islower() is True :
        print(i.upper(),end="")
    else :
        print(i.lower(),end="")
print()