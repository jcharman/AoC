#!/usr/bin/python3

def main():
    
    num_cards = {}
    card_points = {}
    total_cards = 0

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
                    card_total += 1
            card_points[tuple(my_nums)] = card_total
            num_cards[tuple(my_nums)] = 1
            total_cards += 1

    cards = list(num_cards.keys())
    for card in cards:
        index = cards.index(card)
        cards_to_copy = list(range(index+1, index+1+card_points[card]))
        for new_card in cards_to_copy:
            num_cards[cards[new_card]] += (1 * num_cards[card])
        total_cards += (len(cards_to_copy) * num_cards[card])
    print(total_cards)

if __name__ == '__main__':
    main()
