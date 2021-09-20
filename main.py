from MauMau import MauMau
from random_player import RandomPlayer


def main():
    acc_rounds = 0
    player1 = 0
    player2 = 0
    count = 1000
    verbose = False
    for i in range(count):
        game = MauMau([RandomPlayer('Player1', verbose=verbose), RandomPlayer('Player2', verbose=verbose)], verbose=verbose)
        stats = game.run()
        del game
        print(stats)
        acc_rounds += stats[0]
        if stats[1][0].name == 'Player1':
            player1 += 1
        else:
            player2 += 1

    print('Stats:')
    print(f'average game length: {acc_rounds / count} rounds')
    print(f'player1: {player1 / count}')
    print(f'player2: {player2 / count}')


if __name__ == '__main__':
    main()
