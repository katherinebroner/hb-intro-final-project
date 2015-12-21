"Go Fish!" Final Project

Usage:
1. Run file in Python using go_fish.py
2. Python Version 2.7.10

User Flow:

1. Shuffle cards (deck of 52)
2. Pass out 7 cards to each player
3. Player 1 asks for certain rank from Computer (e.g. do you have a 2?)
4. If Computer has the card, give to Player 1. Player 1 asks again.
5. If Computer does not have the card, say "Go Fish", and Player 1 draws a card from the deck
6. Computer asks for certain rank from Player 1
7. If Player 1 has the card, give to Computer. Computer asks again.
8. If Player 1 does not have the card, say "Go Fish", and Computer draws a card from the deck
9. Continue alternating and check for books.
10. When either player collects a book of a certain rank (e.g. all 4's), counts as one point and is set aside
11. The game is over when either player runs out of cards or the deck is empty
12. The winner is the player that has the most points (higher number of books)

Pseudocode:

1. Set up cards.
    1. rank = 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q
    2. shuffle deck = suffle (rank * 4)
    3. distribute 7 cards to each player
    4. remove distributed cards from main deck
    5. add distributed cards to each players hand
    6. set up blank score book for each player (score book will hold all books and keep score, 1 book = 1 point, most points win)

2. Player 1 turn
    1. Show cards player 1 has
        1. check for book: book = 4 of certain rank (e.g. 4 6's)
    2. Player 1 will ask for card in her hand (eg "do you have a 4?")
    3. If Computer has card, give to player 1.  Player 1 asks for another card.
        1. remove card from Computer's hand and add to Player 1's hand
        2. Player 1 check for book
    4. If Computer does not have card, Computer says "Go Fish!" and Player 1 will choose a card from the deck.
        1. Remove chosen card from deck.
        2. Add chosen card to Player 1's hand.
        3. Check for book
    5. After Player 1 draws card, it is the Computer's turn

3. Computer turn
    1. Check for book in Computer's hand.
    2. Computer will ask for card in its hand.
    3. If Player 1 has card, give to Computer.  Computer asks for another card.
        1. remove card from Player 1's hand and add to Computer's hand
        2. Computer check for book
    4. If Player 1 does not have card, Player 1 says "Go Fish!" and Computer will take a card from the deck.
        1. Remove chosen card from deck.
        2. Add chosen card to Computer's hand.
        3. Check for book
    5. After Computer takes card, it Player 1's turn again.

4. Play game
    1. Shuffle and distribute cards (part 1)
    2. Alternate between Player 1's turn and Computer's turn.
        1. If either player has book, remove from hand and put into player score book.
    3. Game is over when player runs out of cards or deck is empty
    4. The winner is the player with the greatest number of points in their scorebook. 
