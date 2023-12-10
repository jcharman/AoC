#!/usr/bin/python3

def main():
    seeds = []
    ranges = {}

    with open('input.txt', 'r') as input_file:
        line = input_file.readline().strip()
        while line != '':
            if line.startswith('seeds:'):
                seeds = [int(seed) for seed in line.split(':')[1].split()]
                input_file.readline()
                line = input_file.readline().strip()
            else:
                map = line.split()[0]
                ranges[map] = {}
                line = input_file.readline().strip()
                while line != '':
                    digits = [int(num) for num in line.split()]
                    dest_range = range(digits[0], digits[0] + digits[2])
                    source_range = range(digits[1], digits[1] + digits[2])
                    ranges[map][source_range] = dest_range
                    line = input_file.readline().strip()
                line = input_file.readline().strip()
    
    locations = []

    for seed in seeds:
        next_val = seed
        for map in ranges:
            for source in ranges[map]:
                if next_val in source:
                    difference = source.start - ranges[map][source].start
                    next_val = next_val - difference
                    break
                else:
                    next_val = next_val

        locations.append(next_val)

    print(min(locations))

if __name__ == '__main__':
    main()