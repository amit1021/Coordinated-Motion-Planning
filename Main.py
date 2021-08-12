from ExtractBoard import ExtractBoard
from StartGame import start_game
from Test import test

if __name__ == '__main__':
    eb = ExtractBoard(7)
    eb.extract_board()
    number_of_steps = start_game(eb)
    test(eb, number_of_steps)
