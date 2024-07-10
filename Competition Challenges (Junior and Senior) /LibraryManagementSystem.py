books = {"Hello": 15, "Hi": 5, "Good morning": 1}

def borrow(book) -> str:
    if book not in books:
        return "Book not in the library"
    if books[book] == 0:
        return "Not enough copies of the book available"
    books[book] -= 1
    return "Have fun while reading the book 😊"

def returnBook(book) -> str:
    if book not in books:
        return "The book is not from our library"
    books[book] += 1
    return "Thanks 😊"

def viewBooks() -> str:
    output = ""
    for name, number in books.items():
        output += f"Book name: {name}, we have {number} books available\n"
    return output

while True:
    print("Choose one of these: borrow a book (1), return a book (2), view books (3), or -1 to end the process: ", end='')
    operation = input()
    if operation == "-1":
        break
    if operation == "1":
        name = input("Enter the name of the book: ")
        print(borrow(name))
    elif operation == "2":
        name = input("Enter the name of the book: ")
        print(returnBook(name))
    elif operation == "3":
        print(viewBooks())
    else:
        print("Invalid operation")
