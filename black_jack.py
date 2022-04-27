
'''
Imports and Global Lists
'''

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

'''
Classes
'''

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
  
    def shuffle(self):
        
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    
    def deal_two(self):
        pop_list = []
        pop_list.append(self.all_cards.pop())
        pop_list.append(self.all_cards.pop())
        return pop_list

class Chip:
    
    def __init__(self,balance):
    
        self.balance=balance
    
    def __str__(self):
        return str(self.balance)
    
    def deposit(self,credit):
        self.balance += credit
        print(f'You have gained {credit} in chips')
    
    def bet(self):

        global answer
        answer = False

        while answer not in range(10,self.balance+1,10):

            answer = int(input(f'Choose a bet (10-{self.balance}): '))  
            #will break if not an integer 

            if answer not in range(10,self.balance+1,10):
                print('Sorry that is an invalid amount.\nPlease choose an amount within your balance and to the nearest 10')
    
        self.balance -= answer
        print(f'Bet of {answer} placed')

class Hand:

    def __init__(self,owner):
        self.owner = owner
        self.my_cards = []
    
    def add_one(self,new_card):
        self.my_cards.append(new_card)

    def add_two(self,new_cards):
        self.my_cards.extend(new_cards)
       
    def __str__(self):
        print(self.owner)
        for i in self.my_cards:
            print(f'{i}')
    
    def sum(self):
        total = 0
        for i in self.my_cards:
            total += i.value
        for i in self.my_cards:
            if total > 21 and i.rank == 'Ace':
                total -= 10
        return total
    
    def hit_stay(self):

        global choice
        choice = 'wrong'

        while choice not in ['H','S']:
            choice = input(f'Hit or Stand? (H or S): ').upper()

            if choice not in ['H','S']:
                print('Sorry that is an invalid input. Please choose H or S')
        return choice
    
    def combine(self,hole_card):
        for x in hole_card:
            self.my_cards.append(x)
          
'''
Game
'''

print('\nWelcome to BlackJack\n')

player_balance = Chip(500)
print(f'You have {player_balance} in chips')

game_on = True

while game_on:

    round_on = True

    while round_on:
        #reset the deck and hands
        new_deck = Deck()
        new_deck.shuffle()
        player_hand = Hand('\nPlayer:')
        dealer_hand = Hand('\nDealer:')
        dealer_hole = Hand('Hole')

        #place a bet
        player_balance.bet()

        #draw the cards and place them into each of the hands
        dealer_hand.add_one(new_deck.deal_one())
        dealer_hole.add_one(new_deck.deal_one())
    
        player_hand.add_two(new_deck.deal_two())

        #print player's and dealer's hands
        dealer_hand.__str__()
        print('Worth: ' + str(dealer_hand.sum()))

        player_hand.__str__()
        print('Worth: '+ str(player_hand.sum()))

        #check for initial blackjack
        if (dealer_hand.sum() == 11) and (dealer_hand.sum() + dealer_hole.sum() == 21):
            dealer_hand.combine(dealer_hole.my_cards)
            dealer_hand.__str__()
            print('Worth: ' + str(dealer_hand.sum()))
            print('\nDealer has a natural BlackJack\nYou lose this round\n')
            round_on = False
            break
        elif player_hand.sum() == 21:
            print('\nYou have a natural BlackJack\nYou win this round!\n')
            player_balance.deposit(2*answer)
            round_on = False

        #begin player hit loop
        if round_on == True:

            hit_loop = True

            while hit_loop == True:
                
                player_hand.hit_stay()
                
                if choice == 'S':
                    hit_loop = False
                    break

                elif choice == 'H':
                    player_hand.add_one(new_deck.deal_one())
                    player_hand.__str__()
                    print('Worth: '+ str(player_hand.sum()))

                    if player_hand.sum() == 21:
                        print('\nYou have BlackJack\nNow for the dealer\n')
                        hit_loop = False
                        break
                    elif player_hand.sum() > 21:
                        print('\nBUST! You lose this round\n')
                        hit_loop = False
                        round_on = False
                        break            
        
        #begin dealer hit loop
        if round_on == True:
        
            dealer_hand.combine(dealer_hole.my_cards)
            
            hit_loop = True

            while hit_loop == True:

                dealer_hand.__str__()
                print('Worth: ' + str(dealer_hand.sum()))
                
                if dealer_hand.sum() == 21 and player_hand.sum() == 21:
                    print("\nYou both have BlackJack\nPUSH!\n")
                    player_balance.deposit(answer)
                    hit_loop = False
                    round_on = False
                elif dealer_hand.sum() == 21:
                    print('\nThe dealer has BlackJack\nYou lose this round!\n')
                    hit_loop = False
                    round_on = False   
                elif dealer_hand.sum() > 21:
                    print('\nDealer has BUST! You win this round\n')
                    player_balance.deposit(2*answer)
                    hit_loop = False
                    round_on = False    
                elif dealer_hand.sum() > player_hand.sum():
                    print(f'\nDealer hand is greater! {dealer_hand.sum()}:{player_hand.sum()}\nYou lose this round!\n')
                    hit_loop = False
                    round_on = False   
                else:
                    dealer_hand.add_one(new_deck.deal_one())
                    continue
                break

    if player_balance.balance == 0:
        print('You are broke! You cannot continue\nYou are the biggest loser!')
        game_on = False
        break

    decision = 'wrong'

    while decision not in ['K','C']:

        decision = input(f'You have {player_balance} in chips\nWould you like to keep going or cash in? (K or C): ').upper()

        if decision not in ['K','C']:
            print('Sorry that is an invalid input. Please choose K or C')
    
    if decision == 'C':      

        if player_balance.balance >= 500:
            print(f'Congradulations, you leave with {player_balance} in chips')
        else:
            print(f"You leave with {player_balance} in chips, that's less than you started with...\nWhat a loser!")

        game_on = False
        break

print('Thank you for playing!')
