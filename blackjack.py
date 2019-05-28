import random
from itertools import product
import click



# determine possible hand values
def hand_values(hand):

   possible_values = []

   # strip suits, replace face cards with 10, and replace Aces with 1
   cards = [c[0] for c in hand]
   card_values = [10 if x in ['J', 'Q', 'K'] else 1 if x == 'A' else int(x) for x in cards]

   possible_values.append(sum(card_values))

   # If the hand contains an Ace, then there are two
   # potentially viable hand values
   if 'A' in cards:
       possible_values.append(sum(card_values) + 10)

   return possible_values


   
# show current chip count, and both hands
# if player has not ended their action loop,
# do not show the dealer's second card
def show_table(d_hand, y_hand, show_dealer, chips):
    
    click.clear()
    click.echo(f'Chips Remaining: {chips}')


    if not show_dealer:
        click.echo(f'Dealer:      {"".join(d_hand[0])}   ??')
    else:
        click.echo(f'Dealer:      {"   ".join(["".join(x) for x in d_hand])}')

    click.echo(f'Your hand:   {"   ".join(["".join(x) for x in y_hand])}')
    click.echo('\n')




# create a new deck of cards
# card suites show unicode characters.  I think
# this is what makes it Windows-specific?
def get_deck(num_decks=1):

    # Create a deck of cards
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * num_decks
    card_suites = [u'\u2665', u'\u2666', u'\u2660', u'\u2663']
    deck = list(product(card_values, card_suites))

    # Shuffle the deck
    random.shuffle(deck)

    return deck



# Initialize a new hand
def deal(num_decks=1):

    deck = get_deck(num_decks)

    dealer_hand = []
    your_hand = []

    # Deal the hands
    your_hand.extend([deck[0], deck[2]])
    dealer_hand.extend([deck[1], deck[3]])

    return your_hand, dealer_hand, deck



