import pickle
import os
def add_record():
    with open("book.dat", "ab") as f:
        n = int(input("Enter book no: "))
        b = input("enter book name: ")
        a = input("enter author name: ")
        p = float(input("enter Price: "))
        l = [n, b, a, p]
        pickle.dump(l, f)

def display_record():
    try:
        with open("book.dat", "rb") as f:
            print("book details:\n")
            while True:
                y = pickle.load(f)
                print(f"book no: {y[0]} book name: {y[1]} author: {y[2]} Price: {y[3]}\n")
    except EOFError:
        print("Reached End-Of-File.")
    except FileNotFoundError:
        print("File not found.")

def book_by_author():
    author = input("enter the author's name: ")
    found = False
    try:
        with open("book.dat", "rb") as f:
            while True:
                y = pickle.load(f)
                if y[2] == author:
                    print(f"the book by {author} is: {y[1]}")
                    found = True
    except EOFError:
        if not found:
            print("o book found  author.")
    except FileNotFoundError:
        print("file not found.")

def book_by_price():
    max_price = float(input("enter the maximum book price: "))
    found = False
    try:
        with open("book.dat", "rb") as f:
            while True:
                y = pickle.load(f)
                if y[3] <= max_price:
                    print(f"{y[1]} - Price: {y[3]}")
                    found = True
    except EOFError:
        if not found:
            print("no books found under that price.")
    except FileNotFoundError:
        print("File not found.")

def copy_data():
    min_price = float(input("enter the minimum price to copy books: "))
    count = 0
    try:
        with open("book.dat", "rb") as f, open("costly_book.dat", "wb") as g:
            while True:
                try:
                    y = pickle.load(f)
                    if y[3] > min_price:
                        l = (y[1], y[3])
                        pickle.dump(l, g)
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("source file not found.")
        return

    if count == 0:
        print("no costly books found.")
    else:
        print(f"{count} costly book(s) copied to costly_book.dat")

    try:
        with open("costly_book.dat", "rb") as f:
            print("Costly Book Records:")
            while True:
                try:
                    y = pickle.load(f)
                    print(f"Book Name: {y[0]} | price: {y[1]}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("Costly book file not found.")

# Menu
while True:
    print("\n1. Insert\n2. Display All\n3. Search by Author\n4. Search by Price\n5. Copy Costly Books\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        display_record()
    elif choice == '3':
        book_by_author()
    elif choice == '4':
        book_by_price()
    elif choice == '5':
        copy_data()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")

