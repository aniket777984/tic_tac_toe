def checkWin(x, y):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        if((x[win[0]] + x[win[1]] + x[win[2]]) == 3):
            print("X Won the match")
            return 1
        if((y[win[0]] + y[win[1]] + y[win[2]]) == 3):
            print("Y Won the match")
            return 0
    return -1

def printCurrentStanding(x, y):
    board = []
    for i in range(1,10,1):
        temp = i
        if x[i] == 1:
            temp = 'X'
        elif y[i] == 1:
            temp = 'Y'
        else:
            pass
        board.append(temp)

    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print(f"--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print(f"--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]} ") 

    
if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for Y
    print("Welcome To The World of Tic-Tac-Toe")
    while(True):
        printCurrentStanding(x, y)

        while(True):
            if(turn == 1):
                print("X's Chance To Enter")
                value = int(input("Please enter a value: "))
                if(y[value] == 1):
                    print("Inavlid Choice --- Enter Again")
                else:
                    x[value] =  1
                    break
            else:
                print("Y's Chance To Enter")
                value = int(input("Please enter a value: "))
                if(x[value] == 1):
                    print("Inavlid Choice --- Enter Again")
                else:
                    y[value] =  1
                    break

        cwin = checkWin(x, y)
        if(cwin != -1):
            printCurrentStanding(x, y)
            print("Match over")
            break
        
        if turn == 1:
            turn = 0
        else:
            turn = 1
             