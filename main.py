from board import Board

print("Zacznijmy gre:")
player = input("Kto ma zacząć X czy O: ")

board = Board(player.upper())

while (not board.check_if_win()) and (not board.check_if_draw()):
    board.show_board()
    x, y = [int(x) for x in input("Podaj wspołżedne pola na którym chcesz postawić X bądź O: ").split()]
    board.put_to_board(x, y)

board.show_board()
print()
if board.check_if_win():
    if board.get_player() == "X":
        print("Wygrał O")
    else:
        print("Wygrał X")
else:
    print("Remis nikt nie wygrał.")