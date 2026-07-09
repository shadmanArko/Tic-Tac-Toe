from board import Board

Trial = 3
User1_Letter = 0
User2_Letter = 0 
Current_User = 0

BoardList = [ [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]
def PrintUpdatedBoard(BoardList, value):
    global Trial
    global User1_Letter

    if Trial == 0:
        for row in BoardList:
            print(row)
    else:
        for i in range(len(BoardList)):
            for j in range(len(BoardList[i])):
                if BoardList[i][j] == value:
                    if(User1_Letter == Current_User):
                        BoardList[i][j] = User1_Letter
                    elif(User2_Letter == Current_User):
                        BoardList[i][j] = User2_Letter
        for row in BoardList:
            print(row)


PrintUpdatedBoard(BoardList, 1)

def GetSymbolFromUser():
    global User1_Letter
    global User2_Letter
    global Current_User
    
    print("Please Enter the Symbol you wanna use during the game")
    Letter = input("X or O ? ")
    
    while(Letter not in "XOE"):
        print("Please choose only from X or O !! ")
        print("or Press E to Exit")
        Letter = input("X or O ? ")
        if Letter == 'E':
            exit()
    
    if Letter == 'X':
        User1_Letter = 'X'
        User2_Letter = 'O'
    else:
        User2_Letter = 'X'
        User1_Letter = 'O'         


def play_game() -> None:
    # take new board

    # ask for Player symbol (ask_player1_symbol())

    # Level the symbol

    # RUN Result Method in a loop until it give result

    # Print Result

    pass