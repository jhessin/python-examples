import pprint
theBoard = {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
        }

def printBoard(board: dict[str, str]):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for', turn + '. Move on which space?')
    while True:
        move = input()
        if move in theBoard:
            theBoard[move] = turn
            break
        else:
            print('Invalid input!')
            print('Valid values are:')
            pprint.pprint(list(theBoard.keys()))
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
