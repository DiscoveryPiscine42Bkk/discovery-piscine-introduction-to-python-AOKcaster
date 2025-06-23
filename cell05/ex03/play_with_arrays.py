#!/bin/python3
array =  [2, 8, 9, 48, 8, 22, -12, 2] 
new = []
print("Original array: ", array)
for i in range(0,len(array)) :
    if array[i] > 5 :
       new.append(array[i] + 2)
print(set(new))