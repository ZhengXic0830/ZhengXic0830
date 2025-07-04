import random

board = [' ' for _ in range(9)]

WIN_COMBOS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def print_board():
    print('\n'.join([
        f" {board[i]} | {board[i+1]} | {board[i+2]} "
        for i in range(0,9,3)
    ]))


def check_winner(sym):
    return any(all(board[i]==sym for i in combo) for combo in WIN_COMBOS)


def available_moves():
    return [i for i,c in enumerate(board) if c==' ']


def player_move():
    while True:
        try:
            move = int(input("Choose position (1-9): "))-1
            if move in available_moves():
                board[move]='X'
                break
        except ValueError:
            pass
        print("Invalid move. Try again.")


def cpu_move():
    move = random.choice(available_moves())
    board[move]='O'


def main():
    print("Tic Tac Toe - You are X, CPU is O")
    while True:
        print_board()
        player_move()
        if check_winner('X'):
            print_board()
            print("You win!")
            break
        if not available_moves():
            print_board()
            print("Draw!")
            break
        cpu_move()
        if check_winner('O'):
            print_board()
            print("CPU wins!")
            break
        if not available_moves():
            print_board()
            print("Draw!")
            break

if __name__ == '__main__':
    main()
