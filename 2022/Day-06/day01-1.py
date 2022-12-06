#!/usr/bin/python3

input = open('input.txt', 'r').readline()

i = 0
different = []
while(len(different) < 4):
    if(input[i] not in different):
        different.append(input[i])
    else:
        different = []
    i += 1

print(i - 1)
