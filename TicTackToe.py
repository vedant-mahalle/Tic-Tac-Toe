def PrintBoard(xchance , zchance):
    zero = "X" if xchance[0] else ("O" if zchance[0] else " ")
    one = "X" if xchance[1] else ("O" if zchance[1] else " ")
    two = "X" if xchance[2] else ("O" if zchance[2] else " ")
    three = "X" if xchance[3] else ("O" if zchance[3] else " ")
    four = "X" if xchance[4] else ("O" if zchance[4] else " ")
    five = "X" if xchance[5] else ("O" if zchance[5] else " ")
    six = "X" if xchance[6] else ("O" if zchance[6] else " ")
    seven = "X" if xchance[7] else ("O" if zchance[7] else " ")
    eight = "X" if xchance[8] else ("O" if zchance[8] else " ")

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def Result(xState, yState):
    x_win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]

    o_win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]

    for condition in x_win_conditions:
        if all(xState[i] == 1 for i in condition):
            return 1  # Player 1 (X) wins

    for condition in o_win_conditions:
        if all(yState[i] == 1 for i in condition):
            return 0  # Player 2 (O) wins

    if all(xState[i] != 0 and yState[i] != 0 for i in range(9)):
        return -1  # It's a draw

    return None  # Game is ongoing
turn = 1 #player X
if __name__=="__main__":
    while True:
        choice = int(input("Enter a Choice\n1.START GAME\n2.RULES\n3.EXIT\n"))
        xState = [0,0,0,0,0,0,0,0,0]
        yState = [0,0,0,0,0,0,0,0,0]
        match choice:
            case 1:
                print(f"   |   |   ")
                print(f"---|---|---")
                print(f"   |   |   ")
                print(f"---|---|---")
                print(f"   |   |   ")
                while True:
                    if turn == 1:
                        xchance = int(input("Player 1 (X) :"))
                        xState[xchance] = 1
                    else:
                        ochance = int(input("Player 2 (O) : "))
                        yState[ochance] = 1
                    win = Result(xState,yState)
                    if(win==1):
                        PrintBoard(xState, yState)
                        print("The Winner is Player 1 ")
                        input("Press any button")
                        break
                    elif(win==0):
                        PrintBoard(xState, yState)
                        print("The winner is Player 2 ")
                        input("Press any button")
                        break
                    elif(win==-1):
                        PrintBoard(xState, yState)
                        print("Its a Tie..")
                        break
                    elif(win==None):
                        turn = 1 - turn
                        PrintBoard(xState, yState)
                        

            case 2 :
                print("Grid Sequence")
                print(f" 0 | 1 | 2 ")
                print(f"---|---|---")
                print(f" 3 | 4 | 5 ")
                print(f"---|---|---")
                print(f" 6 | 7 | 8 ")
                print("Select the box number for you mark")
                input("press anything..")

            case 3 :
                print("Exiting..")
                exit()