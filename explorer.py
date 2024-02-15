import os
import numpy as np

os.system('cls' if os.name == 'nt' else 'clear')
print('Welcome to Explorer - text game')
print('For help enter "help"')

rows = 10
cols = 10

tile = ['void', 'water', 'water',
        'rock', 'rock', 'ground',
        'ground', 'ground', 'ground']

tile2 = ['░','▒','▒','▓','▓','█','█','█','█']

random_array = np.random.randint(0, 9, size=(rows, cols))

def checkPlayerPosition(x, y):
    while x < rows and y < cols and tile[random_array[x, y]] != "ground":
        x += 1
        y += 1
    if x < rows and y < cols:
        return x, y
    else:
        return None

def changeDirection(x, y):
    return x, y

def displayLooking(text, y, x, player_position):
    # os.system('cls' if os.name == 'nt' else 'clear')
    player_position = changeDirection(player_position[0] + x, player_position[1] + y)
    print(f'You look {text}')
    print(f'You see {tile[random_array[player_position]]}')
    if player_position:
        print(f'Player position: {player_position}')
    else:
        print('Player is not on the ground\n')

def moveTo(y, x, player_position):
    new_x = player_position[0] + x
    new_y = player_position[1] + y
    if 0 <= new_x < rows and 0 <= new_y < cols:
        return new_x, new_y
    else:
        return player_position


def printArray(array):
    for row in array:
        print(row)

def printArrayLetters(array):
    for row in array:
        for cell in row:
            first_letter = tile[cell] 
            print(first_letter[0], end=' ')
        print()

def printArrayIcon(array):
    for row in array:
        for cell in row:
            print(tile2[cell], end=' ')
        print()

player_position = checkPlayerPosition(0, 0)

game = True

def whatIsYourAction():
    return str(input("\nYour action: "))

while game:
    action = whatIsYourAction()
    
    if action == 'help':
        print('\ncommands:')
        print('\nla = look around')
        print('\nlw = look at west')
        print('\nle = look at east')
        print('\nln = look at north')
        print('\nls = look at sounth')
        print('\nend = end of game')
        print('\nid = player position (x, y)')
        print('\nhelp = list of command')

    elif action == 'end':
        print('\nGame Over!\n\n')
        game = False

    elif action == 'map':
        printArrayLetters(random_array)
    
    elif action == 'la':
        displayLooking('around.', 0, 0, player_position)

    elif action == 'id':
        print(f'Player position: {player_position}')

    elif action == 'lw':
        displayLooking('at WEST!', -1, 0, player_position)

    elif action == 'le':
        displayLooking('at EAST!', 1, 0, player_position)

    elif action == 'ln':
        displayLooking('at NORTH!', 0, -1, player_position)

    elif action == 'ls':
        displayLooking('at SOUTH!', 0, 1, player_position)

    elif action == 'mw':
        player_position = moveTo(-1, 0, player_position)

    elif action == 'me':
        player_position = moveTo(1, 0, player_position)

    elif action == 'mn':
        player_position = moveTo(0, -1, player_position)

    elif action == 'ms':
        player_position = moveTo(0, 1, player_position)

    else:
        print('Don\'t understand. Again')
