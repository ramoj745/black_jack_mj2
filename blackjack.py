import random
from colorama import init, Fore, Style
init()

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):

        self.allcards = []
        
        for suit in suits:
            for rank in ranks:

                created_cards = Card(suit, rank)

                self.allcards.append(created_cards)

    def shuffle_cards(self):

        random.shuffle(self.allcards)

    def deal(self):

        return self.allcards.pop(0)
       
class Hand:

    def __init__(self):
        self.cards = []  
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value

class Chips():
    
    def __init__(self,total=100, bet=0):
        self.total = total
        self.bet = bet

    def add_total(self,amount):
        self.total += amount
        
    def win_bet(self):
        win = self.bet * 2
        self.total += win
        return win
    
    def lose_bet(self):
        lost = self.bet
        self.total -= lost
        return lost
    

def hit(deck,hand):

    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):

    global playing
    prompt = input("\n(CASE SENSITIVE!) Would you like to hit or stand? (hit or stand): ")
    if prompt == 'hit':
        hit(deck,hand)
        return True
    else:
        playing = False
        return False

def show_some(player,dealer):

    print(colored_green("\nYour Cards:"))
    for cards in player.cards:
        print(cards)
    print(colored_white(f'\nCard Value: {player.value}'))
    
    print(colored_red("\nDealer's Cards:"))
    for cards in dealer.cards:
        if cards == dealer.cards[0]:
            print("[Hidden Card]")
        else:
            print(cards)
    print(colored_white(f'\nCard Value: ?'))
    
def show_all(player,dealer):

    print(colored_green("\nYour Cards:"))
    for cards in player.cards:
        print(cards)
    print(colored_white(f'\nCard Value: {player.value}'))

    print(colored_red("\nDealer's Cards:"))
    for cards in dealer.cards:
        print(cards)
    print(colored_white(f'\nCard Value: {dealer.value}'))

def player_busts():

    print("\nPlayer Bust!")

def player_wins():

    print('\nPlayer won!')
    won = chips.win_bet()

    print()
    print(colored_yellow('*************************************'))
    print(f'You won: {won} {CHIPS}')
    print(f'Your (NEW) total chips: {chips.total}')
    print(colored_yellow('*************************************'))

def dealer_busts():

    print("\nDealer Busts!")
    
def dealer_wins():

    print('\nDealer Wins!')
    lost = chips.lose_bet()

    print()
    print(colored_yellow('*************************************'))
    print(f'You lost: {lost} {CHIPS}')
    print(f'Your (NEW) total chips: {chips.total}')
    print(colored_yellow('*************************************'))
    
def display_chips():
    print("\n"*100)
    print(colored_yellow('*************************************'))
    print(f'Your total chips: {chips.total}')
    print(f'Your current bet: {chips.bet}')
    print(colored_yellow('*************************************'))

def colored_green(text):
    return Fore.GREEN + text + Fore.RESET

def colored_red(text):
    return Fore.RED + text + Fore.RESET

def colored_yellow(text):
    return Fore.YELLOW + text + Fore.RESET

def colored_white(text):
    return Fore.CYAN + text + Fore.RESET

Y = Fore.GREEN + "Y" + Fore.RESET
N = Fore.RED + "N" + Fore.RESET
CHIPS = Fore.YELLOW + "chips!" + Fore.RESET

playing = True

chips_set = False

print(colored_yellow("\nWelcome To BlackJack!"))

while True:

    shuffled_deck = Deck()
    shuffled_deck.shuffle_cards()

    player = Hand()
    dealer = Hand()

    for x in range(2):
        player.add_card(shuffled_deck.deal())
        dealer.add_card(shuffled_deck.deal())

    if chips_set == False:

        prompt3 = input(f"Would you like to set your starting chips (default 100)? ({Y}/{N}): ")

        if prompt3.lower() == 'y':
            chips = Chips()
            chips.total = int(input('Please specify your starting chips: '))
            chips_set = True
        else:
            chips = Chips()
        
    chips.bet = int(input("How much would you like to bet?: "))

    display_chips()
    show_some(player,dealer)


    while playing:

        prompt1 = hit_or_stand(shuffled_deck,player)

        if prompt1 == True:
            display_chips()
            show_some(player,dealer)

        elif prompt1 == False:

            if dealer.value < 17:
                hit(shuffled_deck,dealer)
                display_chips()
                print("\nDealer's cards are lower than 17!")
                print("Dealer adds another card!")
                show_all(player,dealer)

                if player.value > 21:
                    player_busts()
                    dealer_wins()
                    break

                elif dealer.value > 21:
                    dealer_busts()
                    player_wins()
                    break  
                
                if player.value <= 21 and dealer.value <= 21:

                    if player.value > dealer.value:
                        player_wins()
                        break
                    elif dealer.value > player.value:
                        dealer_wins()
                        break
                    elif player.value == dealer.value:
                        print('Tie!')
                        break

            else: 
                display_chips()
                print("\nDealer stands!")
                show_all(player,dealer)

                if player.value > 21:
                    player_busts()
                    dealer_wins()
                    break

                elif dealer.value > 21:
                    dealer_busts()
                    player_wins()
                    break
                
                if player.value <= 21 and dealer.value <= 21:

                    if player.value > dealer.value:
                        player_wins()
                        break
                    elif dealer.value > player.value:
                        dealer_wins()
                        break
                    elif player.value == dealer.value:
                        print('Tie!')
                        break

    prompt2 = input("Would you like to play again? (Y/N): ")
    if prompt2.lower() == 'y':
        playing = True
        continue
    else:
        break
