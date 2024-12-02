#!/usr/bin/python3

from copy import copy

def is_safe(seq: list) -> bool:
    diffs = []
    for i in range(len(seq)):
        if i == 0:
            diffs.append(0)
        else:
            diffs.append(seq[i] - seq[i-1])
    if all(i>0 for i in diffs[1:]) or all(i<0 for i in diffs[1:]):
        abs_diffs = [abs(x) for x in diffs[1:]]
        if not(any(i<1 for i in abs_diffs) or any(i>3 for i in abs_diffs)):
            return True
    return False

if __name__ == '__main__':
    safe = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            data = [int(x) for x in line.strip().split()]
            if is_safe(data):
                safe += 1
            else:
                for i in range(len(data)):
                    tmp_data = copy(data)
                    tmp_data.pop(i)
                    if is_safe(tmp_data):
                        safe+=1
                        break

        print(safe)
