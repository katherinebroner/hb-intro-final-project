#Set up cards

import random
import time

rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck_of_cards = (rank * 4)

random.shuffle(deck_of_cards)

player_1_hand = []

computer_hand = []

player_1_score = []

computer_score = []

def remove_card(random_card):
    deck_of_cards.remove(random_card)

def ask_for_card():
    return raw_input ("What card would you like to ask for? ")

def asked_for_everything(stored_card):
    for i in computer_hand:
        if i not in stored_card:
            return False
    return True


def passing_out_cards():
    player_1_hand.extend(random.sample(deck_of_cards, 7))
    for i in player_1_hand:
        deck_of_cards.remove(i)
    computer_hand.extend(random.sample(deck_of_cards, 7))
    for i in computer_hand:
        deck_of_cards.remove(i)

#passing_out_cards()

#Check for book #book equals four of the same card

def check_for_book(hand, score):
    for i in hand:
        count = hand.count(i)
        if count == 4:
            while i in hand:
                hand.remove(i)
                score.append(i)
            print "There was a book: " + i

#Player 1 turn

def player_1_turn():
    check_for_book(player_1_hand, player_1_score)
    time.sleep(1)  
    while len(player_1_hand) > 0:
        print sorted(player_1_hand)
        ask = ask_for_card()  
        if ask not in computer_hand:
            break
        while ask in computer_hand:
            player_1_hand.append(ask)
            computer_hand.remove(ask)
            time.sleep(1) 
            check_for_book(player_1_hand, player_1_score)
    time.sleep(1)
    print "Go Fish Player 1!"
    time.sleep(1)
    if len(deck_of_cards) > 0:
        random_card = random.choice(deck_of_cards)
        print "Player 1 drew: " + random_card
        player_1_hand.append(random_card)
        remove_card(random_card)
        check_for_book(player_1_hand, player_1_score) 
    else:
        print "Game over!"
        if len(player_1_score) > len(computer_score):
            print "Player 1 wins!"
        elif len(player_1_score) < len(computer_score):
            print "Computer wins!"
        else:
            print "It's a tie!"
    
        
#player_1_turn()

#Computer turn

def computer_turn():
    check_for_book(computer_hand, computer_score)
    time.sleep(1)
    stored_card = []
    while not asked_for_everything(stored_card):
        computer_card = random.choice(computer_hand)
        while computer_card in stored_card:
            computer_card = random.choice(computer_hand)
        stored_card.append(computer_card)
        print "The computer asked for: " + computer_card
        if computer_card not in player_1_hand:
            break
        while computer_card in player_1_hand:
            computer_hand.append(computer_card)
            player_1_hand.remove(computer_card)
        check_for_book(computer_hand, computer_score)
        time.sleep(1)
        while len(computer_hand) < 0:
            break
    time.sleep(1)
    print "Go Fish Computer!"
    time.sleep(1)
    if len(deck_of_cards) > 0:
        random_card = random.choice(deck_of_cards)
        computer_hand.append(random_card)
        remove_card(random_card)
        check_for_book(computer_hand, computer_score)
    else:
        print "Game over!"
        if len(player_1_score) > len(computer_score):
            print "Player 1 wins!"
        elif len(player_1_score) < len(computer_score):
            print "Computer wins!"
        else:
            print "It's a tie!"

#computer_turn()

#Play game

def play_game():
    print "Welcome to Go Fish!"
    print "How to play: Ask the Computer for a card. If you have 4 of the same card, that is a book. The player with the most number of books wins!"
    passing_out_cards()
    while deck_of_cards > 0 and len(player_1_hand) > 0 and len(computer_hand) > 0:
        player_1_turn()
        computer_turn()
   
play_game()












