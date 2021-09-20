import random

import card
import deck
import player


class RandomPlayer(player.Player):

    def turn(self, top: card.Card, rule):
        play = None
        suit = None

        if rule['draw']:
            for card in self.cards:
                if card.rank == '7':
                    play = card
                    self.cards.remove(card)
                    break
            if play and len(self.cards) == 1:
                self.msg('Mau')
            if play and len(self.cards) == 0:
                self.msg('Mau-Mau')
            return [play, suit]

        for card in self.cards:
            if card.rank == top.rank or (not rule['suit'] and (card.suit == top.suit)) or \
                    (rule['suit'] and card.suit == rule['suit']):
                play = card
                self.cards.remove(card)
                break
        if play and play.rank == 'J':
            suit = random.choice(deck.SUITS)

        if play and len(self.cards) == 1:
            self.msg('Mau')
        if play and len(self.cards) == 0:
            self.msg('Mau-Mau')

        return [play, suit]

    def msg(self, msg):
        if self.config['verbose']:
            print(msg)
