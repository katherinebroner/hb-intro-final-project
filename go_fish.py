#Set up cards

import random

rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck_of_cards = rank * 4
random.shuffle(deck_of_cards)
player_1_hand = []
computer_hand = []
player_1_score = []
computer_score = []
def ask_for_card():
    return raw_input ("What card would you like to ask for? ")

def passing_out_cards():
    player_1_hand.extend(random.sample(deck_of_cards, 7))
    for i in player_1_hand:
        deck_of_cards.remove(i)
    computer_hand.extend(random.sample(deck_of_cards, 7))
    for i in computer_hand:
        deck_of_cards.remove(i)

passing_out_cards()

#Player 1 turn

def player_1_turn():
    print player_1_hand
    print computer_hand
    while True:    
        ask = ask_for_card()    
        if ask in computer_hand:
            player_1_hand.extend(ask)
            computer_hand.remove(ask)
            print player_1_hand
        else:
            print "Go Fish!"
            random_card = random.choice(deck_of_cards)
            player_1_hand.append(random_card)
            deck_of_cards.remove(random_card)
            break
    print player_1_hand
        
player_1_turn()



