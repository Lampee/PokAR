import Poker_Game as pk

c1 = pk.Card(pk.Ranks.six, pk.Suits.spades)
c2 = pk.Card(pk.Ranks.two, pk.Suits.hearts)
c3 = pk.Card(pk.Ranks.three, pk.Suits.clubs)
c4 = pk.Card(pk.Ranks.four, pk.Suits.diamonds)
c5 = pk.Card(pk.Ranks.five, pk.Suits.hearts)

h1 = pk.Hand([c1,c2,c3,c4,c5])

h1.print_hand()
print(h1.is_straight())
