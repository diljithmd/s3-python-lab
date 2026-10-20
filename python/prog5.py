import pickle
import os

def add_record():
    with open("book.dat", "ab") as f:
        bookcode = input("Enter book code: ")
        bookname = input("Enter book name: ")
        author = input("Enter author name: ")
        price = float(input("Enter price: "))
        k = [bookcode, bookname, author, price]
        pickle.dump(k, f)
        print("✅ Record added successfully.")

def display_record():
    try:
        with open("book.dat", "rb") as f:
            print("\n📘 All Book Records:")
            while True:
                try:
                    y = pickle.load(f)
                    print(f"Code: {y[0]}, Name: {y[1]}, Author: {y[2]}, Price: ₹{y[3]}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("⚠️ No records found.")

def books_by_author():
    author_name = input("Enter author name: ")
    found = False
    try:
        with open("book.dat", "rb") as f:
            while True:
                try:
                    y = pickle.load(f)
                    if y[2].lower() == author_name.lower():
                        print(f"📖 {y}")
                        found = True
                except EOFError:
                    break
        if not found:
            print("❌ Author not found.")
    except FileNotFoundError:
        print("⚠️ File not found.")

def books_by_price():
    max_price = float(input("Enter price threshold: "))
    found = False
    try:
        with open("book.dat", "rb") as f:
            while True:
                try:
                    y = pickle.load(f)
                    if y[3] > max_price:
                        print(f"💰 {y}")
                        found = True
                except EOFError:
                    break
        if not found:
            print("❌ No books above that price.")
    except FileNotFoundError:
        print("⚠️ File not found.")

def exp_data():
    count = 0
    try:
        with open("book.dat", "rb") as f:
            while True:
                try:
                    y = pickle.load(f)
                    if y[3] > 500:
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("⚠️ File not found.")
    return count

def delete_record():
    bookcode = input("Enter book code to delete: ")
    found = False
    try:
        with open("book.dat", "rb") as f, open("temp.dat", "wb") as t:
            while True:
                try:
                    y = pickle.load(f)
                    if y[0] != bookcode:
                        pickle.dump(y, t)
                    else:
                        found = True
                except EOFError:
                    break
        if found:
            os.remove("book.dat")
            os.rename("temp.dat", "book.dat")
            print("🗑️ Record deleted.")
        else:
            os.remove("temp.dat")
            print("❌ Book code not found.")
    except FileNotFoundError:
        print("⚠️ No records to delete.")

def update_record():
    bookcode = input("Enter book code to update: ")
    found = False
    temp = []
    try:
        with open("book.dat", "rb") as f:
            while True:
                try:
                    y = pickle.load(f)
                    if y[0] == bookcode:
                        print("Current record:", y)
                        bookname = input("Enter new book name: ")
                        author = input("Enter new author name: ")
                        price = float(input("Enter new price: "))
                        updated = [bookcode, bookname, author, price]
                        temp.append(updated)
                        found = True
                    else:
                        temp.append(y)
                except EOFError:
                    break
        if found:
            with open("book.dat", "wb") as f:
                for r in temp:
                    pickle.dump(r, f)
            print("🔄 Record updated.")
        else:
            print("❌ Book code not found.")
    except FileNotFoundError:
        print("⚠️ No records found.")

# 🧭 Menu-driven interface
while True:
    try:
        print("\n📚 Book Management Menu")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Search by Author")
        print("4. Search by Price")
        print("5. Count Books > ₹500")
        print("6. Delete Record")
        print("7. Update Record")
        print("8. Exit")
        choice = int(input("Enter your choice (1–8): "))

        if choice == 1:
            add_record()
        elif choice == 2:
            display_record()
        elif choice == 3:
            books_by_author()
        elif choice == 4:
            books_by_price()
        elif choice == 5:
            count = exp_data()
            print(f"📊 Total books costing more than ₹500: {count}")
        elif choice == 6:
            delete_record()
        elif choice == 7:
            update_record()
        elif choice == 8:
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("⚠️ Please enter a valid number.")