#!/usr/bin/python3

if __name__ == '__main__':
    safe = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            data = [int(x) for x in line.strip().split()]
            diffs = []
            for i in range(len(data)):
                if i == 0:
                    diffs.append(0)
                else:
                    diffs.append(data[i] - data[i-1])
            if all(i>0 for i in diffs[1:]) or all(i<0 for i in diffs[1:]):
                abs_diffs = [abs(x) for x in diffs[1:]]
                if not(any(i<1 for i in abs_diffs) or any(i>3 for i in abs_diffs)):
                    safe += 1
        print(safe)
