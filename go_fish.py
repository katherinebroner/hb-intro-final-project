#Set up cards

import random

rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck_of_cards = (rank * 4)
random.shuffle(deck_of_cards)
player_1_hand = []
computer_hand = []
player_1_score = []
computer_score = []
random_card = random.choice(deck_of_cards)
remove_card = deck_of_cards.remove(random_card)
def ask_for_card():
    return raw_input ("What card would you like to ask for? ")

def passing_out_cards():
    player_1_hand.extend(random.sample(deck_of_cards, 7))
    for i in player_1_hand:
        deck_of_cards.remove(i)
    computer_hand.extend(random.sample(deck_of_cards, 7))
    for i in computer_hand:
        deck_of_cards.remove(i)

#passing_out_cards()

#Check for book #book equals four of the same card

def check_for_book():
    for i in player_1_hand:
        player_1_count = player_1_hand.count(i)
        if player_1_count == 4:
            player_1_hand.remove(i)
            computer_score.extend(i)
    #print player_1_hand

#Player 1 turn

def player_1_turn():
    check_for_book()
    print sorted(player_1_hand)
    while True:    
        ask = ask_for_card()    
        if ask in computer_hand:
            player_1_hand.extend(ask)
            computer_hand.remove(ask)
            check_for_book()
            print sorted(player_1_hand)
        else:
            print "Go Fish Player 1!"
            player_1_hand.append(random_card)
            remove_card
            break
        
#player_1_turn()

#Computer turn

def computer_turn():
    while True:
        computer_card = random.choice(computer_hand)
        print "The computer asked for a " + computer_card
        if computer_card in player_1_hand:
            computer_hand.extend(computer_card)
            player_1_hand.remove(computer_card)
        else:
            print "Go Fish Computer!"
            computer_hand.append(random_card)
            remove_card
            break

#computer_turn()

#Play game

def play_game():
    passing_out_cards()
    while True:
        if deck_of_cards > 0 and player_1_hand > 0 and computer_hand > 0:
            player_1_turn()
            computer_turn()
        else:
            print "Game over!"
            break

play_game()












