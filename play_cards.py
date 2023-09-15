from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Addison")
print(f"d1: {d1}")

print(f"d1.cards: {d1.cards}")

d1.shuffle()

for i in range(5):
    card = d1.draw()
    print(card)
print()
print(f"d1.dealer: {d1.dealer}")

d1.dealer = "Timothy"
print(f"d1.dealer: {d1.dealer}")

# d1.dealer = 5

print(f"d1: {d1}")
print(f"repr(d1): {repr(d1)}")

print(f"len(d1): {len(d1)}")

print(f"d1.get_ranks(): {d1.get_ranks()}")

j1 = JokerDeck("Alvin")
print(f"j1: {j1}")
j1.shuffle()
print(j1.cards)

