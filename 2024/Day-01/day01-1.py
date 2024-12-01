#!/usr/bin/python3

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        l1 = []
        l2 = []
        for line in input_file:
            l1.append(int(line.split()[0]))
            l2.append(int(line.split()[1]))

    l1 = sorted(l1)
    l2 = sorted(l2)

    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])

    print(total)
