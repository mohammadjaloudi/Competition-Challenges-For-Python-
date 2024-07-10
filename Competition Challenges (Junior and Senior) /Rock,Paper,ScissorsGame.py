howToWin = {"Rock" : "Scissors", "Scissors" : "Paper", "Paper" : "Rock"}
moves = ["Rock", "Paper", "Scissors"]

def winner(player1, player2) -> str:
    if player1 == player2:
        return "Draw"
    if howToWin[player1] == player2:
        return "First player won"
    return "Second player won"

player1 = "0"
player2 = "0"
while True:
    if player1 not in moves:
        player1 = input("Enter your move: Rock, Paper, Scissors: ")
        player1 = player1.title()
        if player1 not in moves:
            print("Invalid")
            continue
    if player2 not in moves:
        player2 = input("Enter your move: Rock, Paper, Scissors: ")
        player2 = player2.title()
        if player2 not in moves:
            print("Invalid")
            continue
    print(f"The result is: {winner(player1, player2)}")
    player1 = player2 = "0"
    con = input("Do you want to continue? Enter YES if you want to continue, otherwise enter anything: ")
    if con.upper() != "YES":
        break
