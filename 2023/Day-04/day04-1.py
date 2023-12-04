#!/usr/bin/python3

def main():
    total = 0

    with open('input.txt', 'r') as input_file:
        for line in input_file:
            card_total = 0
            scratchcard = line.split(':')[1]
            winners = scratchcard.split('|')[0].strip().split(' ')
            winners = [winner for winner in winners if winner != '']
            my_nums = scratchcard.split('|')[1].strip().split(' ')
            my_nums = [num for num in my_nums if num != '']

            for num in my_nums:
                if num in winners:
                    if card_total == 0:
                        card_total += 1
                    elif card_total > 0:
                        card_total = card_total * 2
            total += card_total

        print(total)

if __name__ == '__main__':
    main()
