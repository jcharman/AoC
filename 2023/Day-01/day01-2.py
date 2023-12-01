#!/usr/bin/python3

def main():
    valid_digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    with open('input.txt', 'r') as input_file:
        total = 0
        for line in input_file:
            digits = []
            buffer = ''
            for char in line:
                if char.isdigit():
                    digits.append(int(char))
                    buffer = ''
                else:
                    buffer += char
                    if any(num in buffer for num in valid_digits.keys()):
                        for num in valid_digits.keys():
                            if buffer.find(num) > -1:
                                digits.append(valid_digits[num])
                                buffer = buffer[-1:]
            total += int(f'{digits[0]}{digits[-1]}')
        print(total)
        
if __name__ == '__main__':
    main()
