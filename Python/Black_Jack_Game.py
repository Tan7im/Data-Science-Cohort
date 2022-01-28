# A BlackJack Game
'''When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False'''

import random


def score(hand):

    total = 0
    a = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            a += 1
        else:
            total += int(card)
    total += a
    while total+10 <= 21 and a > 0:
        total += 10
        a -= 1
    return total

print('Do you want to play? Y/N')
inp=input()
comp_win = 0
user_win = 0

while inp == 'Y':

    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'J', 'Q', 'K']
    user_hand = [random.choice(list1), random.choice(list1)]
    comp_hand = [random.choice(list1), random.choice(list1)]
    print('The cards you got:  ', user_hand)
    print('The cards computer got:  ', comp_hand)
    total1 = score(user_hand)
    total2 = score(comp_hand)

    if total1 <= 21 and (total1 > total2 or total2 > 21):
        print("You won!")
        user_win += 1
    else:
        print("You Lost!")
        comp_win += 1

    print('You won '+ str(user_win) + ' times.')
    print('Computer won ' + str(comp_win) + ' times.')

    print('Do you want to play? Y/N')
    inp = input()
