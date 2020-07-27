from random import shuffle

# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':1}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    # Instantiate new deck, no user input bc always same
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        # Can't assign shuffle, can only be internally shuffled
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def remove_one(self):
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        if new_cards == type(list):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'

    def shuffle_hand(self):
        shuffle(self.hand)

# while playing:
deck = Deck()
deck.shuffle()
p1_name = input("Enter a name for P1: ")
while True:
    p2_name = input("Enter a name for P2: ")
    if p2_name == p1_name:
        print("Please choose a different name.")
    else:
        break
p1_hand = Hand(p1_name)
p2_hand = Hand(p2_name)

# Give each player half of deck
for x in range(26):
    p1_hand.add_cards(deck.deal_one())
    p2_hand.add_cards(deck.deal_one())

playing = True
round_num = 0
while playing:
    
    round_num += 1
    print(f'Round {round_num}')


    if len(p1_hand.hand) == 0:
        print(f'Player {p1_name} is out of cards! Player {p2_name} wins!')
        break
    elif len(p2_hand.hand) == 0:
        print(f'Player {p1_name} is out of cards! Player {p2_name} wins!')
        break

    print(f'Player {p1_name} has {len(p1_hand.hand)} cards.')
    print(f'Player {p2_name} has {len(p2_hand.hand)} cards.')

    p1_hand.shuffle_hand()
    p2_hand.shuffle_hand()

    p1_card = p1_hand.remove_one()
    p2_card = p2_hand.remove_one()

    at_war = True
    while at_war:
        print(f'Player {p1_name} plays {p1_card}\nPlayer {p2_name} plays {p2_card}')

        if p1_card.value > p2_card.value:
            print(f'Player {p1_name} has the bigger card.')
            p1_hand.add_cards(p2_card)
            p1_hand.add_cards(p1_card)
            at_war = False

        elif p1_card.value < p2_card.value:
            print(f'Player {p2_name} has the bigger card.')
            p2_hand.add_cards(p2_card)
            p2_hand.add_cards(p1_card)
            at_war = False

        else:
            print('Tie! Both players go to war.')
            
            if len(p1_hand.hand) < 6:
                print(f'Player {p1_name} has insufficient cards to go to war.')
                print(f'Player {p2_name} wins!')
                playing = False
                break

            elif len(p2_hand.hand) < 6:
                print(f'Player {p2_name} has insufficient cards to go to war.')
                print(f'Player {p1_name} wins!')
                playing = False
                break

            else:
                p1_cards = []
                p2_cards = []
                for num in range(4):
                    p1_cards.append(p1_hand.remove_one())
                    p2_cards.append(p2_hand.remove_one())
   
                p1_card2 = p1_hand.remove_one()
                p2_card2 = p2_hand.remove_one()

                print(f'Player {p1_name} plays {p1_card2}\nPlayer {p2_name} plays {p2_card2}')

                if p1_card.value > p2_card.value:
                    print(f'Player {p1_name} has the bigger card.')
                    p1_hand.add_cards(p2_card2)
                    p1_hand.add_cards(p1_card2)
                    p1_hand.add_cards(p2_cards)
                    p1_hand.add_cards(p1_cards)

                elif p1_card.value < p2_card.value:
                    print(f'Player {p2_name} has the bigger card.')
                    p2_hand.add_cards(p2_card2)
                    p2_hand.add_cards(p1_card2)
                    p2_hand.add_cards(p2_cards)
                    p2_hand.add_cards(p1_cards)
                break