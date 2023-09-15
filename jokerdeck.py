from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()
        joker1 = Card('Joker', None, 'red')
        joker2 = Card('Joker', None, 'black')
        self._cards.append(joker1)
        self._cards.append(joker2)
        
