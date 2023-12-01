#!/usr/bin/python3

def main():
    with open('input.txt', 'r') as input_file:
        total = 0
        for line in input_file:
            digits = [char for char in line if char.isdigit()]
            total += int(f'{digits[0]}{digits[-1]}')
        print(total)

if __name__ == '__main__':
    main()
