def percentage(number) -> float:
    return (number / 30) * 100

def checkMark(number) -> str:
    if number >= 25:
        return "Excellent."
    if number >= 20:
        return " Very good."
    if number >= 15:
        return "Good."
    return "The student should get redo the test."

while True:
    number = input()
    try:
        number = int(number)
        if number < -1 or number > 30:
            print("Invalid grade!")
            continue
        if number == -1:
            break
        print(f"The result is: {checkMark(number)}")
        print(f"Student's mark i: {round(percentage(number), 2)}")
    except ValueError:
        print("You can't enter a character as a mark.") 
        continue
