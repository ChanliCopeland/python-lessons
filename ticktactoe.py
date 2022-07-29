theBoard = {'t-l': ' ', 't-m': ' ', 't-r': ' ', 'm-l': ' ', 'm-m':
' ', 'm-r': ' ', 'l-l': ' ', 'l-m': ' ', 'l-r': ' '}

def printBoard(board):
    print(board['t-l'] + '|' + board['t-m'] + '|' + board['t-r'])
    print('-+-+-')
    print(board['m-l'] + '|' + board['m-m'] + '|' + board['m-r'])
    print('-+-+-')
    print(board['l-l'] + '|' + board['l-m'] + '|' + board['l-r'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


if __name__ == "__main__":
    printBoard(theBoard)