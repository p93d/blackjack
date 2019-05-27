import random
from itertools import product
import sys
import time
from os import system, name
import click




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


   
   
def show_table(d_hand, y_hand, show_dealer, chips):
    
    click.clear()
    click.echo(f'Chips Remaining: {chips}')


    if not show_dealer:
        click.echo(f'Dealer:      {"".join(d_hand[0])}   ??')
    else:
        click.echo(f'Dealer:      {"   ".join(["".join(x) for x in d_hand])}')

    click.echo(f'Your hand:   {"   ".join(["".join(x) for x in y_hand])}')
    click.echo('\n')





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




"""
# Main Game loop
while True:


    
    bet = 10
    betting = True
    
    # Individual Hand loop
    while True:
    
        show_table(dealer_hand, your_hand, betting, chips)
        
        i = 4
        
        # Check for blackjack - 
        if (max(hand_values(your_hand)) == 21) and i == 4:
        
            sys.stdout.write('You have BLACKJACK')
            sys.stdout.write('\n')
            time.sleep(2)
        
            if max(hand_values(dealer_hand)) == 21:
                sys.stdout.write('...but SO DOES THE DEALER (bummer).  PUSH')
                sys.stdout.write('\n')
                time.sleep(1)
            else:
                sys.stdout.write('... and the dealer does not.  YOU WIN')
                sys.stdout.write('\n')
                chips+=(bet*1.5)
                time.sleep(1)
            break
            
            
        # Check for 21
        if (min(hand_values(your_hand)) == 21) or (max(hand_values(your_hand)) == 21):
            
            sys.stdout.write('You have 21')
            sys.stdout.write('\n')
            your_score = 21
            betting = False
            break
        

        
        if min(hand_values(your_hand)) < 21:
        
            while True:
            
                if i == 4:
                    sys.stdout.write('Choose your action:  Hit (H) / Stay (S) / Double-Down (D) >>> ')
                    your_action = input()
                    if your_action.lower() not in ('h', 's', 'd'):
                        sys.stdout.write('\n')
                        sys.stdout.write('Invalid Response')
                        continue
                    else:
                        break
                else:
                    sys.stdout.write('Choose your action:  Hit (H) / Stay (S) >>> ')
                    your_action = input()
                    if your_action.lower() not in ('h', 's'):
                        sys.stdout.write('\n')
                        sys.stdout.write('Invalid Response')
                        continue
                    else:
                        break
                        
                        
                        
            if your_action.lower() == 's':
                
                if max(hand_values(your_hand)) > 21:
                    your_score = min(hand_values(your_hand))
                else:
                    your_score = max(hand_values(your_hand))
   
                betting = False
                break
                
                
            if your_action.lower() == 'd':
                
                bet*=2
                
                your_hand.append(deck[i])
                i+=1
                
                if max(hand_values(your_hand)) > 21:
                    your_score = min(hand_values(your_hand))
                else:
                    your_score = max(hand_values(your_hand))
                break
   
   
            if your_action.lower() == 'h':
                
                your_hand.append(deck[i])
                i+=1
                continue
   
   
        else:
            sys.stdout.write('BUST.  You lose.')
            sys.stdout.write('\n')
            your_score = -1
            
            break
            
    
    
    betting = False
    
    while True:
    
        if your_score == -1:
            break
    
        show_table(dealer_hand, your_hand, betting, chips)
        
        if (hand_values(dealer_hand) == [7, 17]) or (max(hand_values(dealer_hand)) < 17):
            
            dealer_hand.append(deck[i])
            i+=1
            show_table(dealer_hand, your_hand, betting, chips)
            time.sleep(2)
        
        else:
            break
            
    if max(hand_values(dealer_hand)) > 21:
        dealer_score = min(hand_values(dealer_hand))
    else:
        dealer_score = max(hand_values(dealer_hand))
                    
    if dealer_score > 21:
        dealer_score = 0
        
        
    if dealer_score > your_score:
        sys.stdout.write('You lose')
        sys.stdout.write('\n')
        chips-=bet
    elif dealer_score == your_score:
        sys.stdout.write('PUSH')
        sys.stdout.write('\n')
    else:
        sys.stdout.write('You Win!')
        sys.stdout.write('\n')
        chips+=bet
    
    
    
    
    play_again = input('Press "y" to play again >>>')
    
    if play_again.lower() == "y":
        continue
    else:
        print('thanks for playing!')
        break
   
   
   
"""