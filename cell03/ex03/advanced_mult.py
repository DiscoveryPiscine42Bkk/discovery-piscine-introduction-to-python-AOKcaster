#!/bin/python3
first_number = 0
seconds_number = 0
while first_number < 11 :
    temp ="Table de "+str(first_number)+" : "
    while seconds_number < 11:
        temp += str(first_number*seconds_number)+" "
        seconds_number=seconds_number+1
    print(temp)
    first_number=first_number+1
    seconds_number = 0