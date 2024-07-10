def winner(arr) -> bool:
    if ((arr[0][0] == arr[1][1] == arr[2][2]) or (arr[0][2] == arr[1][1] == arr[2][0])) and (arr[1][1] != '.'):
        return True
    for i in range(3):
        if (arr[i][0] == arr[i][1] == arr[i][2]) and (arr[i][0] != '.'):
            return True
        if (arr[0][i] == arr[1][i] == arr[2][i]) and (arr[0][i] != '.'):
            return True
    return False

def check(x, y, arr) -> list:
    while x < 0 or y < 0 or x > 2 or y > 2 or arr[x][y] != '.':
        print("Invalid position. Please enter again.")
        try:
            x, y = map(int, input("Enter the position (0, 0), (1, 2), etc...: ").split(", "))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            x, y = -1, -1
    return [x, y]

arr = [['.' for _ in range(3)] for _ in range(3)]
turn = {1: "X turn", 0: "O turn"}
play = {1: "X", 0: "O"}

while True:
    for i in range(9):
        print(f"It's {turn[i % 2]}.")
        try:
            x, y = map(int, input("Enter the position (0, 0), (1, 2), etc...: ").split(", "))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            x, y = -1, -1
        ans = check(x, y, arr)
        x, y = ans[0], ans[1]
        arr[x][y] = play[i % 2]
        print("Current game is:")
        for row in arr:
            print(' '.join(row))
        if winner(arr):
            print("X won" if i % 2 == 1 else "O won")
            break
    else:
        print("It's a draw!")
    
    con = input("Do you want to continue? Enter YES if you want to continue, otherwise enter anything: ")
    if con.upper() != "YES":
        break
    else:
        arr = [['.' for _ in range(3)] for _ in range(3)]
