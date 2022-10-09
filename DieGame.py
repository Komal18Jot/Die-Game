"""
Visit all Squares is a roll and move board game
The board in this game is a sequence of squares which are initialized with a value of 0
The number of squares in the board is entered by the player i.e.
The board can be as long as the player wants it to be
The number of sides of a die is also entered by the player 

At the start of the game, the game piece is not on the board
The player rolls a die and moves the game piece onto the square of the board based on the value of the die
Each roll determines a new position for the game piece relative to its old position
After each roll, the game displays the board showing the current position of the
game_piece 
The number of times each square in the board has been visited

In order to win the game
The player must move the game piece onto each square of the board at least once  
The board wraps around, so that the game piece always remains on the board
This allows the player to 
Roll the die
Move the game piece on the board in a circular clockwise fashion
A player loses the game if
the game piece lands on the same square 3 times
"""
import random
GAME_PIECE = '@'
MAX_VISITS = 3
def create_board(size:int)->list:
    '''creates a board with the given size'''
    board = [0] * size
    return board # THROW
def display_board(board:list, current_position:int)->None:
    '''displays the board'''
    display_str = '|'
    for index in range(len(board)):
        if index == current_position:
            display_str = f'{display_str}{GAME_PIECE}{board[index]}|'
        else:
            display_str = f'{display_str}{board[index]}|'
        # print(display_str)
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
    
def roll_die(sides:int)->int:
    ''' returns a number between 1 and number of sides'''
    input('Press enter to roll!')
    number = random.randint(1, sides)
    return number # THROW
def update_board(board:list, current_position:int,value:int)->int:
    ''' updates the board'''
    new_position = (current_position + value) % len(board)
    board[new_position] = board[new_position] + 1
    return new_position
def is_game_over(board:list)->bool:
    '''determines if game is over or not'''
    return MAX_VISITS in board or 0 not in board
def display_result(board:list):
    ''' displays the result'''
    if MAX_VISITS in board:
        print('You lost!')
    else:
        print('You win!')
    
def main()->None:
    game_over = False
    current_position = -1 # position of the GAME_PIECE
    board_size = int(input('What is the board size >'))
    board = create_board(board_size) #CATCH
    display_board(board, current_position)
    sides = int(input('How many sides does your die have ?'))
    while not game_over:
        value = roll_die(sides) #CATCH
        print(f'You have rolled a {value}')
        current_position = update_board(board, current_position,value)
        display_board(board, current_position)
        game_over = is_game_over(board)
    display_result(board)
        
main()