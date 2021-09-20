import card


class Player:
    config = {
        'verbose': True
    }
    name = None
    cards = []

    def __init__(self, name, verbose=True):
        self.name = name
        self.config['verbose'] = verbose

    def turn(self, card: card.Card, rule):
        pass

    def draw(self, card: card.Card):
        self.cards.append(card)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
