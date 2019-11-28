from enum import Enum
import Cards


Ranks = Enum('Ranks', 'one two three four five six seven eight nine ten jack queen king ace none')
Suits = Enum('Suits','hearts diamonds clubs spades none')
Hands = Enum('Hands', 'high_card pair two_pair trips straight flush full_house quads straight_flush royal_flush none')

class poker_card:
    rank = Ranks.none
    suit = Suits.none
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def display(self):
        print(self.rank.name + " of " + self.suit.name)


    


class Hand:
    poker_cards = []
    name = Hands.none.name

    def __init__(self, poker_cards):
        self.poker_cards = poker_cards

    def is_hand(self):
        if len(self.poker_cards) == 5:
            return True
        else:
            return False

    def print_hand(self):
        for c in self.poker_cards:
            c.display()

    def is_straight(self):
        poker_card_values=[]
        for c in self.poker_cards:
            poker_card_values.append(c.rank.value)
        poker_card_values.sort()

        for i in range(4):
            if poker_card_values[i] != poker_card_values[i+1]-1:
                return False
        return True
            
    def count_rank(self,rank):
        counter = 0
        for c in self.poker_cards:
            if c.rank == rank:
                counter+=1
        return counter

    def count_suits(self,suit):
        counter = 0
        for c in self.poker_cards:
            if c.suit == suit:
                counter+=1
        return counter

    def is_royal(self):
        if self.poker_cards[0].value == 10 and self.poker_cards[1].rank.value == 11 and self.poker_card[2].rank.value == 12 and self.poker_cards[3].rank.value == 13 and self.poker_card[4].rank.value == 14:
            return True
        else:
            return False

    def is_flush(self):
        for s in Suits:
            if self.count_suits(s) == 5:
                return True
        return False

    def is_straight_flush(self):
       return self.is_straight() and self.is_flush()

    def is_quads(self):
        for r in Ranks:
            if self.count_rank(r) == 4:
                return True
        return False

    def is_trips(self):
        for r in Ranks:
            if self.count_rank(r) >= 3:
                return True
        return False


    def is_two_pair(self):
        pairs = 0
        for r in Ranks:
            if self.count_rank(r) == 2:
                pairs += 1
            if pairs >= 2:
               return True
        return False

    def is_pair(self):
        for r in Ranks:
            if self.count_rank(r) == 2:
                return True
        return False

    def get_highest(self):
        poker_card_values=[]
        for c in self.poker_cards:
            poker_card_values.append(c.rank.value)
        poker_card_values.sort()
        return poker_card_values[4]





        
            
                

          


   




#functions



        