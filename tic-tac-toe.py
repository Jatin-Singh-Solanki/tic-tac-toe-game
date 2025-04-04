def sum(a, b, c):
    return a + b + c 
    
def printBoard(xState, zState):
    
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):

    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for win in wins :
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the match!")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the match!")
            return 0
    return -1

if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 # 1 for x and 0 for o
        print("WelCome to Tic Tac Toe")
    
        while (True):

            printBoard(xState, zState)

            if (turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value : "))
                xState[value] = 1
            else :
                print("O's Chance")
                value = int(input("Please enter a value : "))
                zState[value] = 1

            cwin = checkWin(xState, zState)
            if(cwin!=-1):
                break


            turn = 1 - turn 
            


# def printBoard(xState, zState):
#     zero = 'X' if xState[0] else ('O' if zState[0] else 0)
#     one = 'X' if xState[1] else ('O' if zState[1] else 1)
#     two = 'X' if xState[2] else ('O' if zState[2] else 2)
#     three = 'X' if xState[3] else ('O' if zState[3] else 3)
#     four = 'X' if xState[4] else ('O' if zState[4] else 4)
#     five = 'X' if xState[5] else ('O' if zState[5] else 5)
#     six = 'X' if xState[6] else ('O' if zState[6] else 6)
#     seven = 'X' if xState[7] else ('O' if zState[7] else 7)
#     eight = 'X' if xState[8] else ('O' if zState[8] else 8)

#     print(f"{zero} | {one} | {two}")
#     print("--|---|---")
#     print(f"{three} | {four} | {five}")
#     print("--|---|---")
#     print(f"{six} | {seven} | {eight}")

# def checkWin(state):
#     winPatterns = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]  # Diagonals
#     ]
#     for pattern in winPatterns:
#         if state[pattern[0]] == state[pattern[1]] == state[pattern[2]] == 1:
#             return True
#     return False

# if __name__ == "__main__":
#     xState = [0] * 9
#     zState = [0] * 9
#     turn = 1  # 1 for X, 0 for O

#     print("Welcome to Tic Tac Toe")

#     while True:
#         printBoard(xState, zState)

#         if turn == 1:
#             print("X's Turn")
#         else:
#             print("O's Turn")

#         while True:
#             try:
#                 value = int(input("Enter a position (0-8): "))
#                 if value < 0 or value > 8 or xState[value] or zState[value]:
#                     print("Invalid move, try again.")
#                 else:
#                     break
#             except ValueError:
#                 print("Please enter a valid number between 0 and 8.")

#         if turn == 1:
#             xState[value] = 1
#             if checkWin(xState):
#                 printBoard(xState, zState)
#                 print("X Wins!")
#                 break
#         else:
#             zState[value] = 1
#             if checkWin(zState):
#                 printBoard(xState, zState)
#                 print("O Wins!")
#                 break

#         turn = 1 - turn  # Switch turn
