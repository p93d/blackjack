import blackjack
import click
import time


# Game Settings
num_decks = 1
starting_chips = 200
bet_value = 10
black_jack_multiplier = 1.0



# Main Game setup
def main(chips=starting_chips,
            show_dealer=False,
            bet=bet_value):

    bjack = False

    # Deal the cards
    player, dealer, deck = blackjack.deal(num_decks)
    current_card = 4

    blackjack.show_table(dealer, player, show_dealer, chips)

    # check for blackjack
    if max(blackjack.hand_values(player)) == 21:

        click.echo('**--..--** BLACKJACK **--..--**')
        time.sleep(2)

        # check if dealer also has 21
        if max(blackjack.hand_values(dealer)) == 21:
            click.echo('...but so does the dealer (bummer).  PUSH')
        else:
            click.echo('... and the dealer does not.  YOU WIN')
            bet*=black_jack_multiplier
            bjack = True

    # main player action loop
    while True:
        blackjack.show_table(dealer, player, show_dealer, chips)
        # Check for 21
        if 21 in blackjack.hand_values(player):
            if not bjack:
                click.echo('You have 21')

            your_score = 21
            break

        # If your hand is less than 21, you can keep playing
        elif min(blackjack.hand_values(player)) < 21:

            # Get user input
            # If this is on the initial deal, the player can double-down
            while True:

                if current_card == 4:
                    your_action = click.prompt('Choose your action:  Hit (H) / Stay (S) / Double-Down (D) >>> ', type=str)
                    
                    if your_action.lower() not in ('h', 's', 'd'):
                        click.echo('Invalid Response')
                        continue
                    else:
                        break
                else:
                    your_action = click.prompt('Choose your action:  Hit (H) / Stay (S) >>> ', type=str)
                    
                    
                    if your_action.lower() not in ('h', 's'):
                        click.echo('Invalid Response')
                        continue
                    else:
                        break

            # User stays - take the highest valid hand value
            if your_action.lower() == 's':
                blackjack.show_table(dealer, player, show_dealer, chips)
                your_score = max([c for c in blackjack.hand_values(player) if c <= 21])
                break

            # If user does not stay then give them a card
            else:
                player.append(deck[current_card])
                current_card += 1

                # if the user doubled-down, double their bet
                # and break the activity loop
                if your_action.lower() == 'd':
                    # double your bet
                    bet *= 2
                    
                    # determine the hand value
                    if [c for c in blackjack.hand_values(player) if c <= 21] == []:
                        your_score = -1
                    else:
                        your_score = max([c for c in blackjack.hand_values(player) if c <= 21])
                    break
                else:
                    continue
            
        # otherwise the player is over 21, and loses
        else:
            click.echo('BUST.  You lose.')
            your_score = -1
            break
    
    # player activity is finished, so we can show the dealer's second card
    show_dealer = True

    # Dealer activity loop
    while True:
    
        # If you have already busted, it doesn't matter
        # what the dealer has, you lose
        if your_score == -1:
            break
        
        # if you have blackjack, we've already checked the dealer's hand
        if bjack:
            break
    
        blackjack.show_table(dealer, player, show_dealer, chips)
        
        # if dealer has a soft 17 or anything less than 16, they will hit
        if (blackjack.hand_values(dealer) == [7, 17]) or (max(blackjack.hand_values(dealer)) < 17):
            
            dealer.append(deck[current_card])
            current_card+=1
            time.sleep(2)
            blackjack.show_table(dealer, player, show_dealer, chips)
        
        # otherwise they will stay
        else:
            break


    # evaluate dealer's hand
    if [c for c in blackjack.hand_values(dealer) if c <= 21] == []:
        dealer_score = -1
    else:
        dealer_score = max([c for c in blackjack.hand_values(dealer) if c <= 21])
       
    
    # see who wins
    if dealer_score > your_score:
        if not bjack:
            click.echo('You lose')
        chips-=bet
    elif dealer_score == your_score:
        if not bjack:
            click.echo('PUSH')
    else:
        if not bjack:
            click.echo('You Win!')
        chips+=bet


    # play again?
    while True:
       
        your_action = click.prompt('Would you like to play again? (y/n) ', type=str)
        
        if your_action.lower() not in ('y', 'n'):
            click.echo('Invalid Response')
            continue
        else:
            break

    if your_action.lower() == 'y':
        main(chips, False, bet_value)
    else:
        click.echo(f'you finished with {chips} chips')
        quit()


main()
