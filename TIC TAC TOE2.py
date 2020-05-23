#Global Variables
import sys

def display_board(board):
    #Function for designing the board
    print ('   |   |   ')
    print ('{}  | {} | {} '.format(board[6],board[7],board[8])) #This is where the X and O will go
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print ('{}  | {} | {} '.format(board[3],board[4],board[5])) #This is where the X and O will go
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print ('{}  | {} | {} '.format(board[0],board[1],board[2])) #This is where the X and O will go
    print ("   |   |   ")

    pass

def player_input():
    #Function for assigning the player whether they will be X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Please choose whether you want X or O: ")
    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1,player2)


def win_condition(board):
    #Check if there's a win on the horizontal axisX
        if board[0] == board[1] == board[2] != " ": #Horizontal Win
            return True
        elif board[3] == board[4] == board[5] != " ": #Horizontal Win
            return True
        elif board[6] == board[7] == board[8] != " ": #Horizontal Win
            return True
        elif board[0] == board[3] == board[6] != " ": #Vertical Win
            return True
        elif board[1] == board[4] == board[7] != " ": #Vertical Win
            return True
        elif board[2] == board[5] == board[8] != " ": #Vertical Win
            return True
        elif board[0] == board[4] == board[8] != " ": #Diagonal Win
            return True
        elif board[2] == board[4] == board[6] != " ": #Diagonal Win
            return True
        else:
            return False


def play_again():
        retry_game = ""
        while retry_game != "Y" or retry_game != "N":
            retry_game = input("Do you want to play again? Y/N ")
            if retry_game == "Y":
                game()
                pass
            if retry_game == "N":
                print ("Thanks for Playing!")
                sys.exit()

def place_marker(board, marker, board_position):
    #This function will grab the user's position
    board[int(board_position)-1] = marker


    # Reset the board
def game():
    board = ([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ])
    testboard = ([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ])
    game_state = True
    turn_state = True
    count = 0

    # This function grabs the player's input whether they want to be X or O
    player1, player2 = player_input()
    marker = player1
    display_board(testboard)  # Displays the entire board blank

    for i in range(10):
        if count%2 == 0:
            marker = player1
            # Assigning the board position to the number the player inputs.
            board_position = int(input("Player 1, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player1)))

        else:
            marker = player2
            # Assigning the board position to the number the player inputs.
            board_position = int(input("Player 2, please enter a number between 1 - 9 to place your {} in the corresponding position. ".format(player2)))

        # This will allow the player to input the positions

        if board[board_position-1] == " ":
            place_marker(board, marker, board_position)
            count += 1
            display_board(board)

        else:
            print ("This place is already filled, please try another position")

        # This function checks for a win.
        if count >= 5:
            if win_condition(board) == True:
                print ("Hooray, {} you won!".format(marker))
                play_again()



        # If all possible moves are made and there are no wins, a tie has been made.
        if count == 9 and win_condition(board) == False:
            print ("Aww, you losers, you tied!")
            play_again()

game()