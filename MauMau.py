import sys

import card
import deck
import player


class MauMau:

    config = {
        'verbose': True,
    }

    deck = None
    players = []
    finishers = []

    def __init__(self, players, verbose=True):
        self.finishers = []
        if len(players) < 2 or len(players) > 5:
            sys.exit("Player count needs to be between 2 and 5!")
        self.players = players
        self.deck = deck.Deck()
        self.config['verbose'] = verbose

    def give_cards(self):
        for player in self.players:
            cards = [self.deck.draw() for _ in range(7)]
            self.msg(f'player {player} draws: {cards}')
            player.cards = cards

    def run(self):
        rule = {
            'draw': 0,
            'skip': 0,
            'suit': None,
        }
        rounds = 0

        self.msg('Game starts')
        self.give_cards()
        self.msg(f'top card is: {self.deck.get_last_discard()}\n')

        while len(self.players) > 1:
            rounds += 1
            for player in self.players:
                self.msg(f'Turn of {player} with {player.cards}, top card {self.deck.get_last_discard()}')

                if rule['skip']:
                    self.msg('skip turn\n')
                    rule = self.reset_rule()
                    continue

                [card, suit] = player.turn(self.deck.get_last_discard(), rule)

                self.msg(f'plays {card}')
                if suit:
                    self.msg(f'next suit is {suit}')

                if rule['draw'] and (card is None or card.rank != '7'):
                    self.msg(f'needs to draw {rule["draw"]} cards')
                    cards = [self.deck.draw() for _ in range(rule['draw'])]
                    self.msg(f'draws {cards}')
                    player.cards.extend(cards)
                    rule = self.reset_rule()
                    self.msg('')
                    continue

                if card is None:
                    card = self.deck.draw()
                    self.msg('did not play any card')
                    self.msg(f'draws card {card}')
                    player.draw(card)
                elif (rule['suit'] and card.suit != rule['suit'] and card.rank != self.deck.get_last_discard().rank) or\
                        (rule['draw'] != 0 and card and card.rank != '7') or\
                        (card.suit != self.deck.get_last_discard().suit and
                         card.rank != self.deck.get_last_discard().rank and not rule['suit']):
                    self.msg(rule)
                    self.msg(f'played nonmatching card: {card}, card on discard pile: {self.deck.get_last_discard()}')
                    if rule['suit']:
                        self.msg(f'suit to be played is {rule["suit"]}')
                    player.draw(card)
                    card = self.deck.draw()
                    self.msg(f'draws extra card {card}')
                    player.draw(card)
                else:
                    self.deck.discard(card)
                    rule = self.get_rule(rule, card, suit)

                self.check_finish(player)
                self.msg('')

        self.finishers.append(self.players[0])
        self.msg(f'Game Ended in {rounds} rounds')
        for i, finisher in enumerate(self.finishers):
            self.msg(f'{i + 1}. Player {finisher}')

        return [rounds, self.finishers]

    @staticmethod
    def reset_rule():
        return {
            'draw': 0,
            'skip': 0,
            'suit': None,
        }

    @staticmethod
    def get_rule(rule, card: card.Card, suit: str):
        return {
            'draw': 0 if card.rank != '7' else rule['draw'] + 2,
            'skip': 1 if card.rank == 'A' else 0,
            'suit': suit if card.rank == 'J' else None,
        }

    @staticmethod
    def has_finished(player: player.Player):
        return len(player.cards) == 0

    def check_finish(self, player: player.Player):
        if MauMau.has_finished(player):
            self.finishers.append(player)
            self.players.remove(player)

    def msg(self, msg):
        if self.config['verbose']:
            print(msg)
