from enum import Enum


Ranks = Enum('Ranks', 'one two three four five six seven eight nine ten jack queen king ace none')
Suits = Enum('Suits','hearts diamonds clubs spades none')
Hands = Enum('Hands', 'high_card pair two_pair trips straight flush full_house quads straight_flush royal_flush none')

class Card:
    rank = Ranks.none
    suit = Suits.none
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def display(self):
        print(self.rank.name + " of " + self.suit.name)


class Hand:
    cards = []
    name = Hands.none.name

    def __init__(self, cards):
        self.cards = cards

    def is_hand(self):
        if len(self.cards) == 5:
            return True
        else:
            return False

    def print_hand(self):
        for c in self.cards:
            c.display()

    def is_straight(self):
        card_values=[]
        for c in self.cards:
            card_values.append(c.rank.value)
        card_values.sort()

        for i in range(4):
            if card_values[i] != card_values[i+1]-1:
                return False
        return True
            

    def count_rank(self,rank):
        counter = 0
        for c in self.cards:
            if c.rank == rank:
                counter+=1
        return counter

    def count_suits(self,suit):
        counter = 0
        for c in self.cards:
            if c.suit == suit:
                counter+=1
        return counter

   




#functions



        