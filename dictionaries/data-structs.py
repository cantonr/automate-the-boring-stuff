import pprint

cat = {'name': 'Zophie', 'age': 7, 'color': 'black'}
allCats = []
allCats.append({'name': 'Jack', 'age': 9, 'color': 'purple'})
allCats.append({'name': 'Picheal', 'age': 1, 'color': 'orange'})
allCats.append({'name': 'Jimbo', 'age': 13, 'color': 'calico'})

print(allCats)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
pprint.pprint(theBoard)

theBoard['top-L'] = 'X'
theBoard['top-M'] = 'X'
theBoard['top-R'] = 'X'
theBoard['mid-L'] = 'O'
theBoard['mid-M'] = 'O'
theBoard['low-R'] = 'O'


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)

print(type(42))
print(type('str'))
print(type(3.14))
print(type(theBoard))
print(type(theBoard['top-L']))
