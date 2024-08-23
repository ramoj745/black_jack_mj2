import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return f"{self.rank}" + " of " + self.suit
    
class Deck():
    def __init__(self):
        
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                
                created_cards = Card(suit, rank)

                self.allcards.append(created_cards)

    def shuffle_deck(self):
       random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.allcards = []

    def add_card(self,card):
        if type(card) == type([]):
            self.allcards.extend(card)
        else:
            self.allcards.append(card)
    
    def remove_one(self):
        return self.allcards.pop(0)
        
    def __str__(self):
        return f'{self.name} has {len(self.allcards)} cards'


#Game

new_deck = Deck()
new_deck.shuffle_deck()

play1 = Player("Player One")
play2 = Player("Player Two")

for x in range(26):
    play1.add_card(new_deck.deal_one())
    play2.add_card(new_deck.deal_one())

game_on = True
rounds = 0

while game_on:

    rounds += 1
    print(f'Round {rounds}')

    if len(play1.allcards) == 0:
        print("Player 1 Has no more cards!")
        game_on = False
        break
    if len(play2.allcards) == 0:
        print("Player 2 Has no more cards!")
        game_on = False
        break


    play1_card = []
    play1_card.append(play1.remove_one())
    play2_card = []
    play2_card.append(play2.remove_one())


    at_war = True

    while at_war:

        if play1_card[-1].value < play2_card[-1].value:
            print("Player 2 Wins")
            play2.add_card(play1_card)
            play2.add_card(play2_card)
            at_war = False
        elif play1_card[-1].value > play2_card[-1].value:
            print("Player 1 Wins")
            play1.add_card(play1_card)
            play1.add_card(play2_card)
            at_war = False
        else: 
            print("WAR!")
            if len(play1.allcards) < 6:
                print('Player 1 Lost! Out of Cards For War!, Player 2 Wins!')
                game_on = False
                break
            elif len(play2.allcards) < 6:
                print('Player 2 Lost! Out of Cards For War!, Player 1 Wins!')
                game_on = False
                break
            else:
                for x in range(6):
                    play1_card.append(play1.remove_one())
                    play2_card.append(play2.remove_one())
