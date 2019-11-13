from Poker_Game import *

c1 = Card(Ranks.six, Suits.hearts)
c2 = Card(Ranks.six, Suits.hearts)
c3 = Card(Ranks.three, Suits.hearts)
c4 = Card(Ranks.three, Suits.hearts)
c5 = Card(Ranks.ace, Suits.hearts)

h1 = Hand([c1,c2,c3,c4,c5])

h1.print_hand()
print(h1.get_highest())
print(h1.is_straight_flush())
