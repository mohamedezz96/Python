from random import randrange

def print_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[0][0]," |   ",board[0][1]," |   ",board[0][2]," |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[1][0]," |   ",board[1][1]," |   ",board[1][2]," |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[2][0]," |   ",board[2][1]," |   ",board[2][2]," |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print()



def user_round(board):
    reference = {"1":(0,0),
                 "2":(0,1),
                 "3":(0,2),
                 "4":(1,0),
                 "5":(1,1),
                 "6":(1,2),
                 "7":(2,0),
                 "8":(2,1),
                 "9":(2,2)}
    print_board(board)  
    move = input("Please Enter your Move Number: ")
    if move not in reference.keys():
        user_round(board)
    else:
        location_index_on_board = reference[move]
        if type(board[location_index_on_board[0]][location_index_on_board[1]]) == int:
            board[location_index_on_board[0]][location_index_on_board[1]] = "O"
        else:
            user_round(board)
    return board


def computer_round(board):
    reference = {"1":(0,0),
                 "2":(0,1),
                 "3":(0,2),
                 "4":(1,0),
                 "5":(1,1),
                 "6":(1,2),
                 "7":(2,0),
                 "8":(2,1),
                 "9":(2,2)}
    computer_move_number = str(randrange(1,10))
    location_index_on_board = reference[computer_move_number]
    if type(board[location_index_on_board[0]][location_index_on_board[1]]) == int:
        board[location_index_on_board[0]][location_index_on_board[1]] = "X"
    else:
        computer_round(board)
    
    return board


def equality(group_lists):
    for i in group_lists:
        if i[0]==i[1]==i[2]=="O":
            return "O"
        elif i[0]==i[1]==i[2]=="X":
            return "X"

    return "draw"       
      

def result(board):
    row = board[:]
    column = [[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]]]
    x = [[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][1],board[2][0]]]
    total = [row,column,x]

    for i in total:
        final_result = equality(i)
        if final_result == "O":
            break
        elif final_result == "X":
            break

    return final_result



 
        


def contains_integer(board):
    for row in board:
        for element in row:
            if type(element)==int:
                return True
    return False











print()
print("Welcome to X-O Game Wish you best of Luck  :)")
print()
board = [[1,2,3],[4,"X",6],[7,8,9]]
game = "on"
while game == "on":
    board = user_round(board)
    final = result(board)
    if final == "O":
        print()
        print_board(board)
        print()
        print("Congratulation!, You Are The Winner")
        game ="off"
        break
    elif final == "X":
        print()
        print_board(board)
        print()
        print("Computer Is The Winner GoodLuck Next Time")
        game = "off"
        break
    elif final == "draw":
        print()
        print_board(board)
        print()
        if contains_integer(board) == False:
            print(" Fine It's Draw")
            game ="off"
            break

    board = computer_round(board)
    final = result(board)
    if final == "O":
        print()
        print_board(board)
        print()
        print("Congratulation!, You Are The Winner")
        game ="off"
        break
    elif final == "X":
        print()
        print_board(board)
        print()
        print("Computer Is The Winner GoodLuck Next Time")
        game = "off"
        break
    elif final == "draw":
        print()
        print_board(board)
        print()
        if contains_integer(board) == False:
            print(" Fine It's Draw")
            game ="off"
            break
