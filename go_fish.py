#Set up cards

import random

rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck_of_cards = rank * 4
random.shuffle(deck_of_cards)
player_1_hand = []
computer_hand = []
player_1_score = []
computer_score = []

def passing_out_cards():
    player_1_hand.extend(random.sample(deck_of_cards, 7))
    for i in player_1_hand:
        deck_of_cards.remove(i)
    computer_hand.extend(random.sample(deck_of_cards, 7))
    for i in computer_hand:
        deck_of_cards.remove(i)

